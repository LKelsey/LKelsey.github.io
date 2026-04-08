---
layout: default
title: Publications
permalink: /publications/
---

# Publications
{: .page-title}

A full, up-to-date list of my publications is available on [ADS](https://ui.adsabs.harvard.edu/public-libraries/AXbFp7rzT2aLpzhpEIiOWQ).

## First-Author Publications

{% for pub in site.data.publications.first_author %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a></div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}), {{ pub.journal }}</div>
</div>
{% endfor %}

## Selected Co-Authored Publications

{% for pub in site.data.publications.selected_coauthor %}
<div class="pub-item">
  <div class="pub-title"><a href="{{ pub.url }}">{{ pub.title }}</a></div>
  <div class="pub-authors">{{ pub.authors }} ({{ pub.year }}){% if pub.journal != "" %}, {{ pub.journal }}{% endif %}</div>
</div>
{% endfor %}

For a complete list, see [my ADS library →](https://ui.adsabs.harvard.edu/public-libraries/AXbFp7rzT2aLpzhpEIiOWQ)
