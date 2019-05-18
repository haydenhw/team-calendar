from flask import render_template, jsonify, request

from app import app
from app.models import User, Sink

@app.route('/')
def index():
    return_data = []
    for user in User.query.all():
        return_data.append(user.email)

    return render_template('index.html', users=return_data), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


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
            'disabled': sink_object.disabled
        })

    return jsonify(return_data)


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

    # # Sink.disabled==True
    # disabled_setting = Sink.query.filter(Sink.disabled==)

    # Sink.query.get(id=sink_id)

    return jsonify(return_data)

@app.route('/rest/v1/sink/<int:sink_id>', methods=['POST'])
def sink_create():
    return 'this works!', 200
