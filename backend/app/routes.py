from flask import render_template, jsonify, request

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


@app.route('/rest/v1/sink', methods=['GET'])
def sink_list():
    return_data = []
    for sink_object in Sink.query.filter(Sink.disabled==False).all():
        return_data.append({
            'id': sink_object.id,
            'locationName': sink_object.name,
            'coordinates': {
                'lat': sink_object.lat,
                'long': sink_object.long,
            },
            'slots': sink_object.slots,
            'price_per_hour': sink_object.price_per_hour,
        })

    return jsonify(return_data)


@app.route('/rest/v1/sink/<int:sink_id>', methods=['PATCH'])
def sink_modify(sink_id):
    Sink.query.get(id=sink_id)


@app.route('/rest/v1/sink/<int:sink_id>', methods=['POST'])
def sink_create():
    return 'this works!', 200
