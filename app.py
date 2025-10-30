# Импортируем основной класс Flask
from flask import Flask, render_template

# Создаём объект приложения
app = Flask(__name__)

# Определяем, что будет на главной странице "/"
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/games")
def MyGame():
    return render_template("games.html")
@app.route("/about_me")
def about_me():
    return render_template("about_me.html")
if __name__ == "__main__":
    app.run(debug=True)