{% extends "public.tpl" %}

{% block content %}
<form method="post">
  <div>
    <label>Логин</label>
    <input type="text" name="login">
  </div>
  <div>
    <label>Пароль</label>
    <input type="password" name="password">
  </div>
  <button type="submit">Войти</button>
</form>
{% endblock %}