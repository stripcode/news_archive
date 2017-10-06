<!DOCTYPE html>
<html lang="ru">
<head>
  <title>admin</title>
</head>
<body>
<!-- begin: menu -->
<div>
  <ul>
    <li>
      <a href="/">Главная</a>
    </li>
    <li>
      <a href="/news/">Новости</a>
    </li>
    <li>
      <a href="/logout/">Выход</a>
    </li>
  </ul>
</div>
<!-- end: menu -->
<!-- begin: content -->
{% block content %}{% endblock %}
<!-- end: content -->
</body>
</html>