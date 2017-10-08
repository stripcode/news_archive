{% extends "admin/private/private.tpl" %}

{% block content %}
<form method="post">
  <div>
    <label for="title">Заголовок</label>
    <input type="text" id="title" name="title" required>
  </div>
  <div>
    <label for="article">Статья</label>
    <textarea id="article" name="article" rows="10" cols="100" required></textarea>
  </div>
  <button type="submit" class="btn">Сохранить</button>
</form>
{% endblock %}