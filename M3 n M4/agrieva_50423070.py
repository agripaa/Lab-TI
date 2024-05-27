from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

@app.route('/<name>')
def my_self(name):
    return f'<h1>My name is {name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)