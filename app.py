# Импортируем основной класс Flask
from flask import Flask, render_template, request
from werkzeug.utils import redirect
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect("games.db") as conn:
        with open("data.sql", "r", encoding="utf-8") as f:
            script = f.read()
            conn.executescript(script)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/games")
def MyGame():
    with sqlite3.connect("games.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, players, playing_time FROM games")
        games = cursor.fetchall()
        upd = 0
    return render_template("games.html", games=games, upd = upd)

@app.route("/about_me")
def about_me():
    return render_template("about_me.html")


@app.route("/add")
def form_add_game():
    return render_template("add.html")


@app.route("/add_games", methods=['POST'])
def add_game():
    title = request.form["title"]
    description_game = request.form["description"]
    number_player = request.form["number_player"]
    playing_time = request.form['playing_time']

    # Выводим в консоль, чтобы убедиться, что данные пришли
    print(f"Получено: {title}, игроков: {number_player}")

    # Сохраняем в БД
    with sqlite3.connect("games.db") as conn:
        conn.execute("""
            INSERT INTO games (title, description, players, playing_time)
            VALUES (?, ?, ?, ?)
        """, (title, description_game, number_player, playing_time))
    return redirect("/add")

@app.route("/update_game", methods = ['POST'])
def up_gam():
    return redirect('/games')

@app.route("/save_update", methods = ['POST'])
def s_u():
    return redirect('/games')

@app.route("/delete_game", methods = ['POST'])
def del_gam():
    number_game = request.form["num_gam"]
    with sqlite3.connect("games.db") as conn:
        conn.execute(f"""DELETE FROM games
            WHERE (id) = {number_game}""")
    return redirect("/games")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)