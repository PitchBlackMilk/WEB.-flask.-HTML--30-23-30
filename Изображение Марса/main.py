from flask import Flask

app = Flask(__name__)


@app.route('/image_mars')
def do_thing():
    with open('index.html', 'r', encoding='utf-8') as html_file:
        return html_file.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
