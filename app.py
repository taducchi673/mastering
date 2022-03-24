from flask import Flask, redirect, render_template, url_for
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

posts = [
    {
        'author': 'ABC',
        'title': 'Blog 1',
        'content': 'First post content',
        'date_posted': 'Today'
    },
        {
        'author': 'Chi Ta Duc',
        'tit/le': 'Blog 2',
        'content': 'Second post content',
        'date_posted': 'Last night'
    }
]

@app.route('/admin')
def hello_admin():
    return "Hello admin Ta Duc Chi"

@app.route("/")
def home():
    return render_template('index.html', posts = posts)


@app.route('/about_me')
def about():
    return render_template('about.html')

@app.route('/ml')
def ml():
    return render_template('ML.html')

@app.route('/contact_me')
def contact():
    return render_template('contact_me.html')

@app.route('/about/<name>')
def hello(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f'<h1>Hello {name}<h1>'

if __name__ == "__app__":
    app.run(debug = True)