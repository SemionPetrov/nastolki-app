# Импортируем основной класс Flask
from flask import Flask, render_template, request
from werkzeug.utils import redirect
import sqlite3

# Создаём объект приложения
app = Flask(__name__)

# Октрывает базу данных
def init_db():
    with sqlite3.connect("games.db") as conn:
        with open("data.sql", "r", encoding="utf-8") as f:
            script = f.read()
            conn.executescript(script)
# Определяем, что будет на главной странице "/"
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/games")
def MyGame():
    with sqlite3.connect("games.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, players FROM games")
        games = cursor.fetchall()  # Получаем все игры
        print("✅ Игры из БД:", games)
    return render_template("games.html", games=games)
@app.route("/about_me")
def about_me():
    return render_template("about_me.html")
@app.route("/add")
def form_add_game():
    return render_template("add.html")
@app.route("/add_games", methods=['POST'])
def add_game():
    title = request.form["title"]
    number_player = request.form["number_player"]

    # Выводим в консоль, чтобы убедиться, что данные пришли
    print(f"Получено: {title}, игроков: {number_player}")

    # Сохраняем в БД
    with sqlite3.connect("games.db") as conn:
        conn.execute("""
            INSERT INTO games (title, players)
            VALUES (?, ?)
        """, (title, number_player))
    return redirect("/add")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)