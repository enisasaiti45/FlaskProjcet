import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, Response

from werkzeug.exceptions import abort

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user

import controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#dump user class
class User(UserMixin):

    def __init__(self, id):
        self.id = id

@app.route('/protected/')
@login_required
def protected():
    return "protected"

@app.route("/login", methods=["GET", "POST"])
def login():
    login_user(User(1))
    return "you are logged in"

@login_manager.user_loader
def user_loader(user_id):
    return User(user_id)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@app.route('/')
def index():
    artists = controller.get_artists()
    return render_template('index.html', artists=artists)



@app.route('/<int:artist_id>')
def artist(artist_id):
    artist = controller.get_artist(artist_id)
    return render_template('artist.html', artist=artist)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']


        controller.create_artist(name, lastname)
        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    artist = controller.get_artist(id)

    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']

        if not name:
            flash('Name is required!')
        else:
            controller.update_artist(id, name, lastname)
            return redirect(url_for('index'))

    return render_template('edit.html', artist=artist)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    controller.delete_artist(id)
    flash('Artist with id "{}"was successfully deleted!'.format(id))
    return redirect(url_for('index'))

@app.route('/artist')
def info():

    albums = controller.get_albums()
    return render_template('artist.html', albums=albums)


@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
