from flask import render_template, jsonify, request
import googlemaps
from dateutil.parser import parse

from app import app, db
from app.models import User, Sink, Event


@app.route('/')
def index():
    return_data = []
    for user in User.query.all():
        return_data.append(user.email)

    return render_template('index.html', users=return_data), 200


@app.route('/event/<int:user_id>')
def get_user_events(user_id):
    user = User.query.filter(User.id==user_id).first()
    events = Event.query.filter(Event.user_id==user_id).all()

    return_data = []
    for event in events:
        return_data.append({
            'name': event.name,
            'description': event.description,
            'start_time': parse(event.start_time).strftime('%A %B %d, %Y %I:%M %p'),
            'end_time': parse(event.end_time).strftime('%A %B %d, %Y %I:%M %p')
        })

    return render_template('events.html', events=return_data, user=user)


def serialize_sink(sink, current_lat=None, current_lng=None):
    sink_dict = {
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

    if current_lat and current_lng and app.config.get('GOOGLE_API_KEY'):
        gmaps = googlemaps.Client(key=app.config['GOOGLE_API_KEY'])
        directions = gmaps.directions(
            f'{sink.lat},{sink.lng}',
            f'{current_lat},{current_lng}',
        )[0]
        legs = directions.get('legs', [])
        if legs:
            distance = legs[0]['distance']['text']
            sink_dict['distance_from_current'] = distance

    return sink_dict


def serialize_event(event):
    return {
        'id': event.id,
        'user_id': event.user_id,
        'name': event.name,
        'start_time': event.start_time,
        'end_time': event.end_time,
        'lat': event.lat,
        'lng': event.lng
    }


@app.route('/rest/v1/event/<int:user_id>', methods=['GET'])
# Queries all events that have a relationship with the specified user_id
def get_events_with_user_id(user_id):
    user_events = []
    for user_event in Event.query.filter(Event.user_id==user_id).all():
        # Need serialize_event method
        user_events.append(serialize_event(user_event))

    return jsonify(user_events)


@app.route('/rest/v1/event', methods=['POST'])
def event_create():
    try:
        new_event = Event(
            user_id=request.json['userId'],
            name=request.json['name'],
            description=request.json['description'],
            start_time=request.json['start_time'],
            end_time=request.json['end_time'],
            lat=request.json['lat'],
            lng=request.json['lng'],
        )
    except KeyError as e:
        missing_key = e.args[0]
        message = f'Key `{missing_key}` not in request'
        return jsonify({
            'success': False,
            'message': message
        }), 400

    db.session.add(new_event)
    db.session.commit()

    return jsonify(serialize_sink(new_event)), 200


@app.route('/rest/v1/sink', methods=['GET'])
def sink_list():
    return_data = []

    try:
        if request.args.get('lat'):
            current_lat = float(request.args.get('lat'))
        else:
            current_lat = None

        if request.args.get('lng'):
            current_lng = float(request.args.get('lng'))
        else:
            current_lng = None
    except ValueError:
        return jsonify({'success': False, 'message': 'Must provide valid floats for lat/lng'}), 400

    for sink_object in Sink.query.filter(Sink.disabled == False).all():
        return_data.append(serialize_sink(sink_object, current_lat, current_lng))

    return jsonify(return_data)


@app.route('/rest/v1/sink/<int:sink_id>', methods=['GET'])
def sink_get(sink_id):
    sink = Sink.query.get(sink_id)

    try:
        if request.args.get('lat'):
            current_lat = float(request.args.get('lat'))
        else:
            current_lat = None

        if request.args.get('lng'):
            current_lng = float(request.args.get('lng'))
        else:
            current_lng = None
    except ValueError:
        return jsonify({'success': False, 'message': 'Must provide valid floats for lat/lng'}), 400

    if sink:
        return jsonify(serialize_sink(sink, current_lat, current_lng))
    else:
        return jsonify({'success': False, 'message': f'Sink with id `{sink_id}` does not exist'}), 404


@app.route('/rest/v1/sink/<int:sink_id>', methods=['PATCH'])
def sink_modify(sink_id):
    """ Queries database for Sink object with ID sink_id and changes the boolean in the disabled column
        If increment and decrement parameters exist as true, increments and decrements the slots quantity accordingly
        Returns new modified object
    """
    modify_this_sink = Sink.query.filter(Sink.id == sink_id).first()
    commit_to_db = False

    if not modify_this_sink:
        return jsonify({
            'success': False,
            'message': "Could not find sink with ID " + str(sink_id) + "."
        }), 404

    # Check to make sure increment and decrement do not both exist

    if 'increment' in request.json and 'decrement' in request.json:
        return jsonify({
            'success': False,
            'message': "Cannot increment and decrement at the same time"
        }), 400

    if 'increment' in request.json:
        if modify_this_sink.slots < modify_this_sink.max_slots:
            modify_this_sink.slots += 1
            commit_to_db = True
        else:
            message = "Slots already full."
            return jsonify({
                'success': False,
                'message': message
            }), 400

    elif 'decrement' in request.json:

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
        modify_this_sink.disabled = disabled_setting
        commit_to_db = True

    if commit_to_db:
        db.session.add(modify_this_sink)
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
