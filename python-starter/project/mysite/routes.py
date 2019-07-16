from flask import render_template

from mysite import app


@app.route('/')
@app.route('/index')
def index():
    title = 'mysite'
    user = {
        'username': 'foosinn',
    }
    return render_template('index.html', title=title, user=user)

@app.route('/conditionals')
def conditionals():
    logged_in = True
    title = 'mysite'
    user = {
        'username': 'foosinn',
    }
    return render_template('conditionals.html', title=title, user=user, logged_in=logged_in)

@app.route('/loop')
def loop():
    title = 'mysite'
    user = {
        'username': 'foosinn',
    }
    things = [
        {'id': 123, 'name': 'the first item', 'price': 100.09},
        {'id': 124, 'name': 'the second item', 'price': 110.09},
        {'id': 125, 'name': 'the third item', 'price': 104.09},
        {'id': 126, 'name': 'the best item', 'price': 9100.09},
        {'id': 127, 'name': 'the worst item', 'price': 999.99},
    ]
    return render_template('loop.html', title=title, user=user, things=things)
