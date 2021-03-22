from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/home/new')
def index():
    return "E-mail"

@app.route('/user/<string:name>/<int:id>')
def index(name,id):
    return "User Page" + name +'' + id

@app.route('/about')
def about():
    return "About page"


if __name__ == "__main__":
    app.run(debug=True)