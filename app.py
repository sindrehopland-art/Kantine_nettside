from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_kantina():  # put application's code here
    return 'Hello kantina!'


if __name__ == '__main__':
    app.run()
