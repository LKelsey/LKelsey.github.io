---
layout: default
title: Publications
permalink: /publications/
---

# Publications
{: .page-title}

Auto-generated from my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/AXbFp7rzT2aLpzhpEIiOWQ).

{%- assign all_pubs = site.data.publications.first_author | concat: site.data.publications.joint_first_author | concat: site.data.publications.coauthor -%}
{%- assign total = all_pubs | size -%}
{%- assign lead = site.data.publications.first_author | size | plus: site.data.publications.joint_first_author.size -%}
{%- assign citations = 0 -%}
{%- for pub in all_pubs -%}{%- assign citations = citations | plus: pub.citations -%}{%- endfor -%}
{%- assign h = 0 -%}
{%- assign rank = 0 -%}
{%- assign ranked = all_pubs | sort: 'citations' | reverse -%}
{%- for pub in ranked -%}{%- assign rank = rank | plus: 1 -%}{%- if pub.citations >= rank -%}{%- assign h = rank -%}{%- endif -%}{%- endfor -%}

<div class="pub-metrics">
  <div class="metric"><span class="metric-num">{{ total }}</span><span class="metric-label">Publications</span></div>
  <div class="metric"><span class="metric-num">{{ lead }}</span><span class="metric-label">First / joint-first author</span></div>
  <div class="metric"><span class="metric-num">{{ citations }}</span><span class="metric-label">Total citations</span></div>
  <div class="metric"><span class="metric-num">{{ h }}</span><span class="metric-label">h-index</span></div>
</div>

## First-Author Publications

{% for pub in site.data.publications.first_author %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a>{% if pub.citations > 0 %} <span style="font-size:0.78rem;color:var(--color-text-light);">({{ pub.citations }} citations)</span>{% endif %}</div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}), {{ pub.journal }}{% if pub.doi %} · <a href="{{ pub.doi }}">DOI</a>{% endif %}</div>
</div>
{% endfor %}

{% if site.data.publications.joint_first_author.size > 0 %}
## Joint First-Author Publications

{% for pub in site.data.publications.joint_first_author %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a>{% if pub.citations > 0 %} <span style="font-size:0.78rem;color:var(--color-text-light);">({{ pub.citations }} citations)</span>{% endif %}</div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}), {{ pub.journal }}{% if pub.doi %} · <a href="{{ pub.doi }}">DOI</a>{% endif %}</div>
</div>
{% endfor %}
{% endif %}

{% if site.data.publications.coauthor.size > 0 %}
## Co-Author Publications

{% assign current_year = "" %}
{% for pub in site.data.publications.coauthor %}
{% assign pub_year = pub.year | append: "" %}
{% if pub_year != current_year %}
{% assign current_year = pub_year %}

### {{ current_year }}

{% endif %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a>{% if pub.citations > 0 %} <span style="font-size:0.78rem;color:var(--color-text-light);">({{ pub.citations }} citations)</span>{% endif %}</div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}), {{ pub.journal }}{% if pub.doi %} · <a href="{{ pub.doi }}">DOI</a>{% endif %}</div>
</div>
{% endfor %}
{% endif %}
