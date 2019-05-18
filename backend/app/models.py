from app import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(2048))
    last_name = db.Column(db.String(2048))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'


class Sink(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(2048), nullable=False)
    lat = db.Column(db.Float, nullable=False, index=True)
    long = db.Column(db.Float, nullable=False, index=True)
    slots = db.Column(db.Integer, nullable=False)
    disabled = db.Column(db.Boolean, index=True)
    price_per_hour = db.Column(db.Float)

