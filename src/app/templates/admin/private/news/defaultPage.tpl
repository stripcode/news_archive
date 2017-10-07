{% extends "admin/private/private.tpl" %}

{% block content %}
<a href="/news/create/">Создать новость</a>

<ul>
  {% for article in articles %}
  <li>
    <a href="/news/{{ article._id }}">{{ article.title }}</a>
  </li>
  {% endfor %}
</ul>
{% endblock %}