from app import db
# from datetime import datetime

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(2048))
    last_name = db.Column(db.String(2048))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'


class Sink(db.Model):

    __tablename__ = 'sink'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(2048), nullable=False)
    lat = db.Column(db.Float, nullable=False, index=True)
    lng = db.Column(db.Float, nullable=False, index=True)
    max_slots = db.Column(db.Integer, nullable=False)
    slots = db.Column(db.Integer, nullable=False)
    disabled = db.Column(db.Boolean, index=True)
    price_per_hour = db.Column(db.Float)

    def __repr__(self):
        return f'<Sink name {self.name} has {self.slots} slots>'

class Event(db.Model):

    __tablename__ = 'event'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer,
        db.ForeignKey('user.id'), 
        nullable=False)
    user = db.relationship('User', backref='user')
    name = db.Column(db.String(2048), nullable=False)
    start_time = db.Column(db.String(2048), nullable=False)
    end_time = db.Column(db.String(2048), nullable=False)
    lat = db.Column(db.Float, nullable=False, index=True)
    lng = db.Column(db.Float, nullable=False, index=True)

    def __repr__(self):
        return f'<Event {self.name}, User {self.user.first_name}>'