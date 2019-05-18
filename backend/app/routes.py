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
        If increment and decrement parameters exist as true, increments and decrements the slots quantity accordingly
        Returns new modified object
    """
    modify_this_sink = Sink.query.filter(Sink.id==sink_id).first()

    commit_to_db = False

    if not modify_this_sink:
        return jsonify({
            'success': False,
            'message': "Could not find sink with ID " + str(sink_id) + "."
        }), 404

    if request.json.get('increment') == True: 
        print("Increment is true!")
        if modify_this_sink.slots < modify_this_sink.max_slots:
            modify_this_sink.slots += 1
            commit_to_db = True
        else: 
            message = "Slots already full."
            return jsonify({
                'success': False,
                'message': message
            }), 400

    elif request.json.get('decrement') == True: 
        print("Decrement is true!")
        if modify_this_sink.slots > 0:
            modify_this_sink.slots -= 1
            commit_to_db = True
        else: 
            message = "Slots empty, cannot decrement."
            return jsonify({
                'success': False,
                'message': message
            }), 400

    # Get disabled setting from post data from request
    disabled_setting = request.json.get('disabled')

    # Check to see if disabled parameter exists, if it does then change it to disabled_setting
    if 'disabled' in request.json:
        print("'Disabled' parameter exists!")
        modify_this_sink.disabled = disabled_setting
        commit_to_db = True

    if commit_to_db:
        db.session.add(modify_this_sink)
        db.session.commit()

    return jsonify(serialize_sink(modify_this_sink))

# patch with increment, decrement, disabled

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
