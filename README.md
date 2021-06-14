# FlaskProjcet

## Installation


```pip install -r requirements.txt
```

## Usage

```from flask import Flask, render_template, request, url_for, flash, redirect, Response
return render_template('artist.html', albums=albums)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
db = SQLAlchemy(app)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
