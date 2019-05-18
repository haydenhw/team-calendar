
# Team Calendar Backend

## Dev setup

You'll need python3/pip3 setup on your instance.
Usually it's just brew install python3

```bash
cd backend
pip3 install --upgrade virtualenv
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

To run the application:

```bash
python run.py
```

Then, go to localhost:8080 to get a dummy index page
If you go to localhost:8080/rest/v1/sink you'll get the sink list