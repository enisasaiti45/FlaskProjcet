# FlaskProjcet

## Installation
```bash
pip install -r requirements.txt
```

## Usage

```python
from flask import Flask, render_template, request, url_for, flash, redirect, Response
return render_template('artist.html', albums=albums)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
db = SQLAlchemy(app)

```

## Parts of code

```python
def artist(artist_id):
    artist = controller.get_artist(artist_id)
    return render_template('artist.html', artist=artist)


def create():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']

        controller.create_artist(name, lastname)
        return redirect(url_for('index'))

    return render_template('create.html')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
