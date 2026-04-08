#!/usr/bin/env python3
"""
Fetch publications from an ADS public library and update _data/publications.yml.

Usage:
    export ADS_DEV_KEY="your-api-token"
    python update_pubs.py

The script:
  1. Fetches bibcodes from a public ADS library
  2. Queries ADS for full metadata
  3. Writes _data/publications.yml for Jekyll
"""

import os
import sys
import requests
from datetime import datetime, timezone

# ── Configuration ──────────────────────────────────────────────────────────
ADS_LIBRARY_ID = "AXbFp7rzT2aLpzhpEIiOWQ"
ADS_TOKEN = os.environ.get("ADS_DEV_KEY", "")
AUTHOR_NAMES = ["Kelsey, L.", "Kelsey, Lisa"]
OUTPUT_FILE = "_data/publications.yml"
ADS_API = "https://api.adsabs.harvard.edu/v1"
# ───────────────────────────────────────────────────────────────────────────

HEADERS = {
    "Authorization": f"Bearer {ADS_TOKEN}",
    "Content-Type": "application/json",
}


def get_library_bibcodes(library_id: str) -> list[str]:
    """Fetch all bibcodes from a public ADS library."""
    bibcodes = []
    start = 0
    rows = 100

    while True:
        url = f"{ADS_API}/biblib/libraries/{library_id}?start={start}&rows={rows}"
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        data = resp.json()

        docs = data.get("documents", [])
        if not docs:
            break

        bibcodes.extend(docs)
        start += rows

        num_docs = data.get("metadata", {}).get("num_documents", 0)
        if start >= num_docs:
            break

    return bibcodes


def get_paper_metadata(bibcodes: list[str]) -> list[dict]:
    """Fetch metadata for a list of bibcodes via bigquery."""
    fields = [
        "bibcode", "title", "author", "pub", "year", "pubdate",
        "volume", "page", "doi", "citation_count", "property",
        "doctype", "bibstem",
    ]

    bigquery_headers = {
        "Authorization": f"Bearer {ADS_TOKEN}",
        "Content-Type": "big-query/csv",
    }

    resp = requests.post(
        f"{ADS_API}/search/bigquery",
        headers=bigquery_headers,
        data="bibcode\n" + "\n".join(bibcodes),
        params={
            "q": "*:*",
            "fl": ",".join(fields),
            "rows": len(bibcodes),
            "sort": "pubdate desc",
        },
    )
    resp.raise_for_status()
    return resp.json().get("response", {}).get("docs", [])


def is_refereed(paper: dict) -> bool:
    props = paper.get("property", [])
    return "REFEREED" in props


def is_first_author(paper: dict) -> bool:
    """Check if any of the target names match the first author."""
    authors = paper.get("author", [])
    if not authors:
        return False
    first = authors[0].lower()
    return any(first.startswith(name.lower()) for name in AUTHOR_NAMES)


def is_joint_first_author(paper: dict) -> bool:
    """Check if the target author is a joint first author (second position)."""
    authors = paper.get("author", [])
    if len(authors) < 2:
        return False
    second = authors[1].lower()
    return any(second.startswith(name.lower()) for name in AUTHOR_NAMES)


def format_authors_short(paper: dict) -> str:
    """Format a short author string, handling joint first authorship."""
    authors = paper.get("author", [])
    if not authors:
        return ""
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"

    # Joint first author: show both names
    if is_joint_first_author(paper):
        return f"{authors[0]} & {authors[1]} et al."

    return f"{authors[0]} et al."


def format_journal(paper: dict) -> str:
    """Format journal reference."""
    parts = []
    pub = paper.get("pub", "")
    if pub:
        parts.append(pub)
    vol = paper.get("volume", "")
    if vol:
        parts.append(vol)
    page = paper.get("page", [])
    if page:
        parts.append(str(page[0]))
    return ", ".join(parts)


def ads_url(bibcode: str) -> str:
    return f"https://ui.adsabs.harvard.edu/abs/{bibcode}/abstract"


def doi_url(paper: dict) -> str:
    dois = paper.get("doi", [])
    if dois:
        return f"https://doi.org/{dois[0]}"
    return ""


def yaml_escape(s: str) -> str:
    """Escape a string for safe YAML output."""
    if not s:
        return '""'
    escaped = s.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'


def paper_to_yaml(paper: dict, indent: str = "    ") -> str:
    """Convert a paper dict to a YAML entry."""
    title = paper.get("title", ["Untitled"])[0]
    authors_short = format_authors_short(paper)
    journal = format_journal(paper)
    year = paper.get("year", "")
    bibcode = paper.get("bibcode", "")
    citations = paper.get("citation_count", 0) or 0
    doi = doi_url(paper)
    url = ads_url(bibcode)

    lines = [
        f"{indent}- title: {yaml_escape(title)}",
        f"{indent}  authors: {yaml_escape(authors_short)}",
        f"{indent}  year: {year}",
        f"{indent}  journal: {yaml_escape(journal)}",
        f"{indent}  url: {url}",
        f"{indent}  bibcode: {yaml_escape(bibcode)}",
        f"{indent}  citations: {citations}",
    ]
    if doi:
        lines.append(f"{indent}  doi: {doi}")

    return "\n".join(lines)


def generate_yaml(papers: list[dict]) -> str:
    """Generate the full YAML content."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Three-way split: first-author, joint first-author (2nd position), co-author
    first = [p for p in papers if is_first_author(p)]
    joint = [p for p in papers if not is_first_author(p) and is_joint_first_author(p)]
    coauthor = [p for p in papers if not is_first_author(p) and not is_joint_first_author(p)]

    sections = [f"# Auto-generated from ADS library on {now}", f"# Do not edit manually\n"]

    sections.append("first_author:")
    if first:
        for p in first:
            sections.append(paper_to_yaml(p))
    else:
        sections.append("    []")

    sections.append("\njoint_first_author:")
    if joint:
        for p in joint:
            sections.append(paper_to_yaml(p))
    else:
        sections.append("    []")

    sections.append("\ncoauthor:")
    if coauthor:
        for p in coauthor:
            sections.append(paper_to_yaml(p))
    else:
        sections.append("    []")

    return "\n".join(sections) + "\n"


def main():
    if not ADS_TOKEN:
        print("Error: set ADS_DEV_KEY environment variable", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching library {ADS_LIBRARY_ID}...")
    bibcodes = get_library_bibcodes(ADS_LIBRARY_ID)
    print(f"Found {len(bibcodes)} papers")

    if not bibcodes:
        print("No papers found, skipping generation")
        sys.exit(0)

    print("Fetching metadata...")
    papers = get_paper_metadata(bibcodes)
    print(f"Retrieved metadata for {len(papers)} papers")

    papers.sort(key=lambda p: p.get("pubdate", "0000-00"), reverse=True)

    yaml_content = generate_yaml(papers)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(yaml_content)

    first_count = sum(1 for p in papers if is_first_author(p))
    joint_count = sum(1 for p in papers if not is_first_author(p) and is_joint_first_author(p))
    co_count = len(papers) - first_count - joint_count
    print(f"Written to {OUTPUT_FILE}: {first_count} first-author, {joint_count} joint first-author, {co_count} co-author")


if __name__ == "__main__":
    main()
