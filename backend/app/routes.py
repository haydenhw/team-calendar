from flask import render_template, jsonify, request

from app import app, db
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


def serialize_sink(sink):
    return {
        'id': sink.id,
        'locationName': sink.name,
        'coordinates': {
            'lat': sink.lat,
            'lng': sink.lng,
        },
        'slots': sink.slots,
        'price_per_hour': sink.price_per_hour,
        'disabled': sink.disabled
    }


@app.route('/rest/v1/sink', methods=['GET'])
def sink_list():
    return_data = []
    for sink_object in Sink.query.filter(Sink.disabled==False).all():
        return_data.append(serialize_sink(sink_object))

    return jsonify(return_data)


@app.route('/rest/v1/sink/<int:sink_id>', methods=['PATCH'])
def sink_modify(sink_id):
    Sink.query.get(id=sink_id)


@app.route('/rest/v1/sink', methods=['POST'])
def sink_create():
    try:
        new_sink = Sink(
            name=request.json['name'],
            lat=request.json['coordinates']['lat'],
            lng=request.json['coordinates']['lng'],
            slots=request.json['slots'],
            price_per_hour=request.json['price'],
        )
    except KeyError as e:
        missing_key = e.args[0]
        if missing_key == 'lat' or missing_key == 'lng':
            message = f'You need to set `{missing_key}` inside a coordinates object'
        else:
            message = f'Key `{missing_key}` not in request'
        return jsonify({
            'success': False,
            'message': message
        }), 400

    db.session.add(new_sink)
    db.session.commit()

    return serialize_sink(new_sink), 200
