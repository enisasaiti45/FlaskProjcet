from model import Artist, Album
from app import db

def get_artists():
    return Artist.query.all()

def get_artist(artist_id):
    return Artist.query.filter_by(id = artist_id).first()

def create_artist(name, lastname):
    artist = Artist(name=name, lastname=lastname)
    db.session.add(artist)
    db.session.commit()

def update_artist(artist_id, name, lastname):
    artist = get_artist(artist_id)
    artist.name = name
    artist.lastname = lastname
    db.session.commit()

def delete_artist(artist_id):
    artist = get_artist(artist_id)
    db.session.delete(artist)
    db.session.commit()


