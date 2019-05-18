import os
import json
from datetime import datetime

import dateutil.parser
from pytz import timezone, utc

from app import app, db
from app.models import User, Sink, Event


def convert_time_to_utc(year, month, day, hour, minute):
    naive_time = datetime(year, month, day, hour, minute)
    pacific = timezone("US/Pacific")
    timezone_time = pacific.localize(naive_time)
    utc_time = timezone_time.astimezone(utc)
    return utc_time.isoformat()


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

    event1 = Event(
      name="Work", 
      start_time=convert_time_to_utc(2019, 5, 18, 9, 0), 
      end_time=convert_time_to_utc(2019, 5, 18, 16, 30), 
      user_id=default.id, 
      lat="37.803915", 
      lng="-122.271021"
    )

    event2 = Event(
      name="Shopping", 
      start_time=convert_time_to_utc(2019, 5, 18, 17, 0), 
      end_time=convert_time_to_utc(2019, 5, 18, 18, 0), 
      user_id=default.id, 
      lat="37.771311", 
      lng="-122.192745"
    )

    event3 = Event(
      name="Warriors Game", 
      start_time=convert_time_to_utc(2019, 5, 18, 18, 30), 
      end_time=convert_time_to_utc(2019, 5, 18, 21, 30), 
      user_id=default.id, 
      lat="37.750080", 
      lng="-122.203034"
    )
    
    db.session.add(event1)
    db.session.add(event2)
    db.session.add(event3)
    db.session.commit()

    app.run(host='localhost', port=8080, debug=True)
