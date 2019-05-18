import os
import json

from app import app, db
from app.models import User, Sink, Event

SINK_LOCATIONS = json.loads("""
[
  {
    "coordinates": {
      "lat": 37.811161, 
      "lng": -122.262722
    }, 
    "locationName": "Bird", 
    "price_per_hour": 1.90, 
    "slots": 2
  },
  {
    "coordinates": {
      "lat": 37.80908,
      "lng": -122.265588
    }, 
    "locationName": "Lime", 
    "price_per_hour": 2.10, 
    "slots": 3
  },
  {
    "coordinates": {
      "lat": 37.811894,
      "lng": -122.269
    }, 
    "locationName": "Scoot",
    "price_per_hour": 3.30, 
    "slots": 4
  },
  {
    "coordinates": {
      "lat": 37.810148,
      "lng": -122.273045
    }, 
    "locationName": "Nisan",
    "price_per_hour": 5.0, 
    "slots": 1
  },
  {
    "coordinates": {
      "lat": 37.808029,
      "lng": -122.272251
    }, 
    "locationName": "Mitsubishi",
    "price_per_hour": 4.10, 
    "slots": 1
  },
  {
    "coordinates": {
      "lat": 37.808555,
      "lng": -122.269858
    }, 
    "locationName": "Bird", 
    "price_per_hour": 1.90, 
    "slots": 1
  },
  {
    "coordinates": {
      "lat": 37.806716,
      "lng": -122.268699
    }, 
    "locationName": "Lime", 
    "price_per_hour": 2.10, 
    "slots": 1
  },
  {
    "coordinates": {
      "lat": 37.80597,
      "lng": -122.271875
    }, 
    "locationName": "Scoot", 
    "price_per_hour": 3.30, 
    "slots": 1
  },
  {
    "coordinates": {
      "lat": 37.806521,
      "lng": -122.265051
    }, 
    "locationName": "Mitsubishi", 
    "price_per_hour": 4.10, 
    "slots": 1
  },
  {
    "coordinates": {
      "lat": 37.804893,
      "lng": -122.266853
    }, 
    "locationName": "Bird", 
    "price_per_hour": 1.90, 
    "slots": 3
  }
]
""")

if __name__ == '__main__':
    if os.path.exists('app.db'):
        os.remove('app.db')
    db.create_all()

    default = User(email="solaruser@gmail.com", first_name="Solar", last_name="User")
    db.session.add(default)
    db.session.commit()

    for location in SINK_LOCATIONS:
        sink = Sink(
            name=location["locationName"],
            lat=location["coordinates"]["lat"],
            lng=location["coordinates"]["lng"],
            disabled=False,
            price_per_hour=0,
            slots=location["slots"],
            max_slots=location["slots"],
        )
        db.session.add(sink)

    event1 = Event(name= "Event1", start_time = "starttime", end_time = "endtime", user_id = default.id, lat="37.803915", lng="-122.271021")
    event2 = Event(name= "Event2", start_time = "starttime2", end_time = "endtime2", user_id = default.id, lat="37.803621", lng="-122.2706387")
    event3 = Event(name= "Event3", start_time = "starttime3", end_time = "endtime3", user_id = default.id, lat="37.8037411", lng="-122.2834014")
    
    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.commit()

    app.run(host='localhost', port=8080, debug=True)
