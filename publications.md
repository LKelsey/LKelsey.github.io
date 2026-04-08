---
layout: default
title: Publications
permalink: /publications/
---

# Publications
{: .page-title}

Auto-generated from my [ADS library](https://ui.adsabs.harvard.edu/public-libraries/AXbFp7rzT2aLpzhpEIiOWQ).

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
