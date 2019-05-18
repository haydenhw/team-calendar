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


@app.route('/rest/v1/sink/<int:sink_id>', methods=['PATCH'])
def sink_modify(sink_id):
    """ Queries database for Sink object with ID sink_id and changes the boolean in the disabled column
        Returns new modified object
    """

    print(request.json)

    # Get ID from post data from request

    disabled_setting = request.json.get('disabled')
<<<<<<< Updated upstream
    print(disabled_setting)
    # # Find Sink in table with this ID
    modify_this_sink = Sink.query.filter(Sink.id==sink_id).first()

    # # If sink with this ID exists..
    # # get the disabled attribute
    if modify_this_sink:
=======
    
    # # Find Sink in table with this ID 
    modify_this_sink = Sink.query.filter(Sink.id==sink_id).first()

    # # If sink with this ID exists, get the disabled attribute 
    if modify_this_sink: 
>>>>>>> Stashed changes
        modify_this_sink.disabled = disabled_setting
        db.session.add(modify_this_sink)

    else:
        return jsonify({
            'success': False,
            'message': "Could not find sink with ID " + str(sink_id)
        }), 404

    db.session.commit()

<<<<<<< Updated upstream
    return jsonify(serialize_sink(modify_this_sink))


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
=======
    # Make dictionary of modified sink's values are return that
    return_data = {
        'id': modify_this_sink.id,
        'locationName': modify_this_sink.name,
        'coordinates': {
            'lat': modify_this_sink.lat,
            'long': modify_this_sink.long,
        },
        'slots': modify_this_sink.slots,
        'price_per_hour': modify_this_sink.price_per_hour,
        'disabled': modify_this_sink.disabled_setting
    }

    return jsonify(return_data)
>>>>>>> Stashed changes

    return serialize_sink(new_sink), 200
