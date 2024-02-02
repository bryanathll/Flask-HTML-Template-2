from flask import Flask, redirect, url_for 

userApp =False

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello world!!</h1>"

@app.route('/name')
def user():
    return f'<h1>Hello Bryan</h1>'

@app.route('/admin')
def admin():
    if userApp == False:
        return redirect(url_for("user"))
    else:
        return "404 user not found"


if __name__ == '__main__':
    app.run()