# 📊 Лабораторная работа №9  
## Веб-приложение на Flask (To-Do List)

---

## 📌 Цель работы

Создать веб-приложение на Python с использованием фреймворка Flask, корректно организовать структуру проекта и реализовать базовую логику взаимодействия с пользователем.

---

## 🧠 Описание приложения

Разработано простое веб-приложение "To-Do List", которое позволяет:

- добавлять задачи  
- просматривать список задач  
- удалять задачи  

Данные хранятся во временном списке (без базы данных).

---

## 📂 Структура проекта

    lab9/
    │
    ├── app.py
    ├── requirements.txt
    │
    ├── templates/
    │   ├── base.html
    │   └── index.html
    │
    └── static/
        └── style.css

---

## 📦 Установка

Установите Flask:

    pip install flask

---

## 🚀 Запуск приложения

1. Перейдите в папку проекта  
2. Запустите файл:

    python app.py

3. Откройте браузер и перейдите по адресу:

    http://127.0.0.1:5000/

---

## 💻 Основной код (app.py)

    from flask import Flask, render_template, request, redirect

    app = Flask(__name__)

    tasks = []

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            task = request.form.get("task")

            if task and task.strip():
                tasks.append(task.strip())

            return redirect("/")

        return render_template("index.html", tasks=tasks)


    @app.route("/delete/<int:task_id>")
    def delete(task_id):
        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
        return redirect("/")


    if __name__ == "__main__":
        app.run(debug=True)

---

## 🌐 Шаблоны

Файл templates/base.html:

    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask To-Do</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>

    <div class="container">
        {% block content %}{% endblock %}
    </div>

    </body>
    </html>

Файл templates/index.html:

    {% extends "base.html" %}

    {% block content %}

    <h1>📝 To-Do List</h1>

    <form method="POST">
        <input type="text" name="task" placeholder="Введите задачу" required>
        <button type="submit">Добавить</button>
    </form>

    <ul>
        {% for task in tasks %}
            <li>
                {{ task }}
                <a href="/delete/{{ loop.index0 }}">❌</a>
            </li>
        {% endfor %}
    </ul>

    {% if not tasks %}
        <p>Нет задач</p>
    {% endif %}

    {% endblock %}

---

## 🎨 Стили

Файл static/style.css:

    body {
        font-family: Arial;
        background: #f5f5f5;
    }

    .container {
        width: 400px;
        margin: 50px auto;
        background: white;
        padding: 20px;
        border-radius: 10px;
    }

    h1 {
        text-align: center;
    }

    form {
        display: flex;
        gap: 10px;
    }

    input {
        flex: 1;
        padding: 8px;
    }

    button {
        padding: 8px;
    }

    ul {
        margin-top: 20px;
    }

    li {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    a {
        color: red;
        text-decoration: none;
    }

---

## ✅ Выполненные требования

- создано веб-приложение на Flask  
- реализована логика работы приложения  
- используются HTML-шаблоны  
- используется CSS  
- реализована маршрутизация  
- соблюдена структура проекта  

---

## 🚀 Заключение

В ходе лабораторной работы было создано веб-приложение с использованием Flask.  
Реализована работа с формами, шаблонами и маршрутизацией.

---

## 📌 Вывод

Flask позволяет быстро создавать веб-приложения на Python и является удобным инструментом для разработки серверной логики.