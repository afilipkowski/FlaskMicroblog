from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Alek'}
    posts = [
        {
            'author': {'username' : 'Ziutek'},
            'body': 'siema eniu'
        },

        {
            'author': {'username' : 'Ziom'},
            'body': 'elo'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

