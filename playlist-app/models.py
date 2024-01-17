"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist model."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    songs = db.relationship('Song', secondary='playlists_songs', backref='playlists_in_playlist')


class Song(db.Model):
    """Song model."""

    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)

    playlists = db.relationship('Playlist', secondary='playlists_songs', backref='songs_in_song')

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song model."""

    __tablename__ = "playlists_songs"

    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
