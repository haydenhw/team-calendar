from app import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Sink(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(2048), nullable=False)
    lat = db.Column(db.Float, nullable=False, index=True)
    long = db.Column(db.Float, nullable=False, index=True)
