import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', stylesheets="index.css")

@app.route("/portfolio")
def portfolio():
    return flask.render_template("portfolio.html")

@app.route("/commissions")
def commissions():
    pass

if __name__ == '__main__':
    app.run(debug=True)