from flask import Flask


app = Flask(__name__)


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
def contact():
    return '<h3>Contact Us if in need of help</h3>'


@app.route('/users/<name>')
def user(name):
    return "<h3>Welcome {}</h3>".formate(name)


if __name__ == '__main__':
    app.run(debug=True)