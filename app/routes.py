from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Enrique'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in San Francisco!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers thoooo!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)