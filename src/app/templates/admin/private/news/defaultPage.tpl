{% extends "admin/private/private.tpl" %}

{% block content %}
<h2>Новости</h2>
<a href="/news/create/" class="btn btn-primary">Создать новость</a>

<ul>
  {% for article in articles %}
  <li>
    <a href="/news/{{ article._id }}">{{ article.title }}</a>
  </li>
  {% endfor %}
</ul>
{% endblock %}