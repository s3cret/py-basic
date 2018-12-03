from flask import Flask
from flask import request
# usually when you want to retrieve data from
# user's request, use request.form['key']
# to get it, see 23, 24

app = Flask('HackApplication')

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/login', methods=['GET'])
def login_form():
    return '''<form action="/login" method="post">
        <p><input name="username"></p>
        <p><input name="password" type="password"></p>
        <p><button type="submit">Sign In</button></p>
        </form>'''

@app.route('/login', methods=['POST'])
def logedin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return '<h3>Hello, admin!</h3>'
    else:
        return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()

