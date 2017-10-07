<!DOCTYPE html>
<html lang="ru">
<head>
  <title>admin</title>
  <link rel="stylesheet" href="/static/vendor.css">
</head>
<body>
<!-- begin: menu -->
<div class="main">
  <div>
    <ul class="main-menu">
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
  <div class="content">
  {% block content %}{% endblock %}
  </div>
  <!-- end: content -->
</div>
</body>
</html>