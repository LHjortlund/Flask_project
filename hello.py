from flask import Flask


app = Flask(__name__)


def make_bold(f):
    def wrapper1():
        return f'<b>{f()}</b>'

    return wrapper1


def make_emphasis(f):
    def wrapper2():
        return f'<em>{f()}</em>'

    return wrapper2


def make_underlined(f):
    def wrapper3():
        return f'<u>{f()}</u>'

    return wrapper3

@app.route('/')
def index():
    return ('<h1 style="text-align: center">Learning Flask</h1>'
            '<p>Learn More Be Smart</p>'
            '<img src="https://d2zp5xs5cp8zlg.cloudfront.net/image-61785-800.jpg">')

@app.route('/about')
def about():
    return ('<h3>Now we are learning about flask</h3>'
            '<iframe src="https://giphy.com/embed/Ow7TbhjmovnmhBomuN" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/halloween-creepy-spooky-Ow7TbhjmovnmhBomuN">via GIPHY</a></p>')


@app.route('/contact')
@make_bold
@make_emphasis
@make_underlined
def contact():
    return '<h1 style="text-align: center">Contact Us if in need of help</h1>'


@app.route('/users/<name>')
def user(name):
    return "<h3 >Welcome {}</h3>".formate(name)


if __name__ == '__main__':
    app.run(debug=True)