---
layout: default
title: Outreach & Public Engagement
permalink: /outreach/
---

# Outreach & Public Engagement
{: .page-title}

## Kilonova Seekers

I co-created and co-lead [Kilonova Seekers](https://www.zooniverse.org/projects/tkillestein/kilonova-seekers), a citizen science project on the Zooniverse where the public helps the [GOTO collaboration](https://goto-observatory.org/) discover transient events in real time.

<div class="highlight-box">
Kilonova Seekers was awarded the <strong>2025 UKRI Future Leaders Fellowship Public Engagement Award</strong> and has resulted in two publications, two Astronomer's Telegrams, and over 200 reports to the Transient Name Server. <a href="https://goto-obs.github.io/knseekers-results/">See our discoveries →</a>
</div>

[Get involved at kilonova-seekers.org →](https://kilonova-seekers.org)

The project has been used for workshops for primary and secondary school children, and forms the basis of the [IRIS pilot project Multi Messengers](https://researchportal.port.ac.uk/en/publications/multi-messengers/).

## Kilonova Seekers – LCO: STAR

Surveying Transients with Amateur Researchers (STAR) was a [Las Cumbres Observatory Global Sky Partner](https://lco.global/education/partners/) extension of Kilonova Seekers. Citizen scientists decided which transient discoveries to observe with the LCO telescope network, triggered observations, created light-curves, and produced colour images, guided by a lead observer from the project's volunteers.

## 4MOST Science Communication

I co-lead the science communication working group for [4MOST](https://www.4most.eu/). I coordinated all public-facing activities for 4MOST First Light, including international press coverage and social media strategy. I oversee a team of ~10 working on social media channels, newsletters, website content, and educational resources.

## Public Talks

{% for talk in site.data.talks %}
<div class="talk-item">
  <div class="talk-title">{% if talk.url %}<a href="{{ talk.url }}">{{ talk.title }}</a>{% else %}{{ talk.title }}{% endif %}</div>
  <div class="talk-venue">{{ talk.venue }} · {{ talk.date }}</div>
</div>
{% endfor %}

<div class="video-embed">
  <iframe src="https://www.youtube.com/embed/2xz9-BPD6Rc" allowfullscreen loading="lazy"></iframe>
</div>

## Media

{% for item in site.data.media %}
<div class="media-item">
  <span class="media-outlet">{{ item.outlet }}</span>
  <span class="media-date">{{ item.date }}</span>
  — {% if item.url %}<a href="{{ item.url }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}
</div>
{% endfor %}
