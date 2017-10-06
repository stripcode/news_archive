{% extends "admin/public/public.tpl" %}

{% block content %}
<form method="post">
  <div>
    <label for="login" >Логин</label>
    <input type="text" id="login" name="login">
  </div>
  <div>
    <label for="password">Пароль</label>
    <input type="password" id="password" name="password">
  </div>
  <button type="submit">Войти</button>
</form>
{% endblock %}