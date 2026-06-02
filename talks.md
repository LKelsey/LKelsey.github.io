---
layout: default
title: Talks
permalink: /talks/
---
# Talks
{: .page-title}
{% assign now = 'now' | date: '%s' | plus: 0 %}
## Invited Talks & Seminars
{% assign current_year = "" %}
{% for talk in site.data.conference_talks.invited %}
{% assign talk_year = talk.year | append: "" %}
{% if talk_year != current_year %}
{% assign current_year = talk_year %}
### {{ current_year }}
{% endif %}
{% assign ts = talk.date | date: '%s' | plus: 0 %}
<div class="talk-item">
  <div class="talk-title">{{ talk.title }}{% if talk.type == "flash" %} <span style="font-size:0.78rem;color:var(--color-text-light);">(Flash Talk)</span>{% endif %}{% if ts > now %} <span class="talk-scheduled" style="font-size:0.78rem;color:var(--color-text-light);">(scheduled)</span>{% endif %}</div>
  <div class="talk-venue">{{ talk.venue }}{% if talk.note %} · <em>{{ talk.note }}</em>{% endif %}</div>
</div>
{% endfor %}
## Contributed Talks
{% assign current_year = "" %}
{% for talk in site.data.conference_talks.contributed %}
{% assign talk_year = talk.year | append: "" %}
{% if talk_year != current_year %}
{% assign current_year = talk_year %}
### {{ current_year }}
{% endif %}
{% assign ts = talk.date | date: '%s' | plus: 0 %}
<div class="talk-item">
  <div class="talk-title">{{ talk.title }}{% if talk.type == "flash" %} <span style="font-size:0.78rem;color:var(--color-text-light);">(Flash Talk)</span>{% endif %}{% if ts > now %} <span class="talk-scheduled" style="font-size:0.78rem;color:var(--color-text-light);">(scheduled)</span>{% endif %}</div>
  <div class="talk-venue">{{ talk.venue }}{% if talk.note %} · <em>{{ talk.note }}</em>{% endif %}</div>
</div>
{% endfor %}
