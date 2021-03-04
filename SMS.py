from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_sms():
    return "Hello world!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
