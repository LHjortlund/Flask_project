from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Learning Flask</h1><p>Learn More Be Smart</p>'


@app.route('/about')
def about():
    return '<h3>Now we are learning about flask</h3>'


@app.route('/contact')
def contact():
    return '<h3>Contact Us if in need of help</h3>'


@app.route('/users/<name>')
def user(name):
    return "<h3>Welcome {}</h3>".formate(name)


if __name__ == '__main__':
    app.run(debug=True)