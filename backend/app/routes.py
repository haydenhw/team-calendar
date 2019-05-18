from flask import render_template, jsonify

from app import app
from app.models import User, Sink


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return_data = []
    for user in User.query.all():
        return_data.append(user.email)

    return render_template('index.html', users=return_data), 200


@app.route('/rest/v1/sink', methods = ['GET'])
def sink():
    return_data = []
    for sink in Sink.query.all():
        return_data.append({
            'id': sink.id,
            'locationName': sink.name,
            'coordinates': {
                'lat': sink.lat,
                'long': sink.long,
            }
        })

    return jsonify(return_data)
