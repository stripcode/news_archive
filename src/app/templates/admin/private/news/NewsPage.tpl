{% extends "admin/private/private.tpl" %}

{% block content %}
<h2>{{ article.title }}</h2>
<a href="/news/{{ article._id }}/edit/" class="btn">Редактировать</a>
<p>
  {{ article.article }}
</p>
{% endblock %}