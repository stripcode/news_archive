{% extends "admin/private/private.tpl" %}

{% block content %}
<h2>{{ article.title }}</h2>
<p>
  {{ article.article }}
</p>
{% endblock %}