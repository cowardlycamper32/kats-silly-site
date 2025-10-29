import flask
import os

app = flask.Flask(__name__)

class Image:
    def __init__(self, src, name):
        self.image = src
        self.name = name

@app.route('/')
def index():
    return flask.render_template('index.html', stylesheets="index.css")

@app.route("/portfolio")
def portfolio():
    images = []
    for file in os.listdir("static/images"):
        images.append(Image("images/" + file, file))
    return flask.render_template("portfolio.html", images=images)

@app.route("/commissions")
def commissions():
    pass

if __name__ == '__main__':
    app.run(debug=True)