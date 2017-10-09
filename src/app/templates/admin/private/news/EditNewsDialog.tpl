{% extends "admin/private/private.tpl" %}

{% block content %}
<form method="post">
  <div class="form-group">
    <label for="title">Заголовок</label>
    <input type="text" id="title" name="title" value="{{ article.title }}" required>
  </div>
  <div class="form-group">
    <label for="content">Статья</label>
    <textarea id="content" name="content" rows="10" cols="100" required>{{ article.content }}</textarea>
  </div>
  <button type="submit" class="btn btn-primary">Сохранить</button>
</form>
{% endblock %}