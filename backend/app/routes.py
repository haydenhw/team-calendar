from flask import render_template, jsonify, request

from app import app, db
from app.models import User, Sink

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
        'max_slots': sink.max_slots,
        'price_per_hour': sink.price_per_hour,
        'disabled': sink.disabled
    }


@app.route('/rest/v1/sink', methods=['GET'])
def sink_list():
    return_data = []
    for sink_object in Sink.query.filter(Sink.disabled==False).all():
        return_data.append(serialize_sink(sink_object))

    return jsonify(return_data)


@app.route('/rest/v1/sink/<int:sink_id>', methods=['GET'])
def sink_get(sink_id):
    sink = Sink.query.get(sink_id)
    if sink:
        return jsonify(serialize_sink(sink))
    else:
        return jsonify({'success': False, 'message': f'Sink with id `{sink_id}` does not exist'}), 404


@app.route('/rest/v1/sink/<int:sink_id>', methods=['PATCH'])
def sink_modify(sink_id):
    """ Queries database for Sink object with ID sink_id and changes the boolean in the disabled column
        Returns new modified object
    """

    print(request.json)

    # Get ID from post data from request

    disabled_setting = request.json.get('disabled')
    print(disabled_setting)
    # # Find Sink in table with this ID
    modify_this_sink = Sink.query.filter(Sink.id==sink_id).first()

    # # If sink with this ID exists..
    # # get the disabled attribute
    if modify_this_sink:
        modify_this_sink.disabled = disabled_setting
        db.session.add(modify_this_sink)

    else:
        return jsonify({
            'success': False,
            'message': "Could not find sink with ID " + str(sink_id)
        }), 404

    db.session.commit()

    return jsonify(serialize_sink(modify_this_sink))


@app.route('/rest/v1/sink', methods=['POST'])
def sink_create():
    try:
        new_sink = Sink(
            name=request.json['locationName'],
            lat=request.json['coordinates']['lat'],
            lng=request.json['coordinates']['lng'],
            slots=request.json['slots'],
            max_slots=request.json.get('max_slots', request.json['slots']),
            price_per_hour=request.json['price_per_hour'],
            disabled=request.json.get('disabled', False),
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

    return jsonify(serialize_sink(new_sink)), 200
