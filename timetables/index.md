---
title: Timetables
layout: default
---

{% for file in site.static_files %}
    {% if file.path contains "/timetables/" and file.extname == ".ics" %}
        [file.basename]({{ site.baseurl }}{{ file.path }})
    {% endif %}
{% endfor %}