from web import web
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return web.index_fnc()


if __name__ == "__main__":
    app.run(port=8080,debug=True)
