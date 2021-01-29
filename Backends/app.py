from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/main')
def main_web():
    return 'Đây là kết quả khi chạy gọi localhost:9000/main'


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return "your username is : "+str(user)


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
