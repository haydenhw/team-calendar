import os
import json

from app import app, db
from app.models import User, Sink

SINK_LOCATIONS = json.loads("""
[
  {
    "coordinates": {
      "lat": 37.811161, 
      "long": -122.262722
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

    for location in SINK_LOCATIONS:
        sink = Sink(
            name=location["locationName"],
            lat=location["coordinates"]["lat"],
            lng=location["coordinates"]["lng"],
            disabled=False,
            price_per_hour=0,
            slots=1,
            max_slots=1,
        )
        db.session.add(sink)

    db.session.commit()
    app.run(host='localhost', port=8080, debug=True)
