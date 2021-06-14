from app import db

class Artist(db.Model):

    tablename = "artist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text)
    albs = db.relationship('Album', backref='artist', lazy='select')
    songs = db.relationship('Song', backref='artist', lazy='select')

    def repr(self):
        return '<Artist %r>' % self.name


class Production(db.Model):

    tablename = "production"
    production_id = db.Column(db.Integer, primary_key=True)
    production_name = db.Column(db.Text, nullable=False)
    production_owner = db.Column(db.Text, nullable=False)
    albs = db.relationship('Album', backref='production', lazy='select')

    def repr(self):
        return '<Production %r>' % self.production_name


class Album(db.Model):

    tablename = "album"
    album_id = db.Column(db.Integer, primary_key=True)
    album_name = db.Column(db.Text, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    production_id = db.Column(db.Integer, db.ForeignKey('production.production_id'), nullable=False)
    songs = db.relationship('Song', backref='album', lazy='select')

    def repr(self):
        return '<album %r>' % self.album_name




class Song(db.Model):
    tablename = "song"
    song_id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.Text, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.album_id'), nullable=False)

    def repr(self):
        return '<Song %r>' % self.song_name