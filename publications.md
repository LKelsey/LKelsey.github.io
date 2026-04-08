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

