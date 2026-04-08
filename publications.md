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

{% if site.data.publications.coauthor.size > 0 %}
## Co-Author Publications

{% for pub in site.data.publications.coauthor %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a>{% if pub.citations > 0 %} <span style="font-size:0.78rem;color:var(--color-text-light);">({{ pub.citations }} citations)</span>{% endif %}</div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}), {{ pub.journal }}{% if pub.doi %} · <a href="{{ pub.doi }}">DOI</a>{% endif %}</div>
</div>
{% endfor %}
{% endif %}

{% if site.data.publications.non_refereed.size > 0 %}
## Non-Refereed

{% for pub in site.data.publications.non_refereed %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a></div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}), {{ pub.journal }}{% if pub.doi %} · <a href="{{ pub.doi }}">DOI</a>{% endif %}</div>
</div>
{% endfor %}
{% endif %}
