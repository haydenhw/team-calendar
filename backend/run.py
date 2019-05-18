import os
import json

from app import app, db
from app.models import User, Sink

SINK_LOCATIONS = json.loads("""
[
  {
    "locationName": "Bird",
    "coordinates": {
      "lat": 37.811161,
      "lng": -122.262722
    }
  },
  {
    "locationName": "Lime",
    "coordinates": {
      "lat": 37.80908,
      "lng": -122.265588
    }
  },
  {
    "locationName": "Scoot",
    "coordinates": {
      "lat": 37.811894,
      "lng": -122.269
    }
  },
  {
    "locationName": "Nisan",
    "coordinates": {
      "lat": 37.810148,
      "lng": -122.273045
    }
  },
  {
    "locationName": "Nisan",
    "coordinates": {
      "lat": 37.808029,
      "lng": -122.272251
    }
  },
  {
    "locationName": "Bird",
    "coordinates": {
      "lat": 37.808555,
      "lng": -122.269858
    }
  },
  {
    "locationName": "Lime",
    "coordinates": {
      "lat": 37.806716,
      "lng": -122.268699
    }
  },
  {
    "locationName": "Scoot",
    "coordinates": {
      "lat": 37.80597,
      "lng": -122.271875
    }
  },
  {
    "locationName": "Nisan",
    "coordinates": {
      "lat": 37.806521,
      "lng": -122.265051
    }
  },
  {
    "locationName": "Nisan",
    "coordinates": {
      "lat": 37.804893,
      "lng": -122.266853
    }
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
            long=location["coordinates"]["lng"],
            disabled=False,
            price_per_hour=0,
            slots=1,
        )
        db.session.add(sink)

    db.session.commit()
    app.run(host='localhost', port=8080, debug=True)
