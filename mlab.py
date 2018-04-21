import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds251819.mlab.com:51819/project_earth_hero

host = "ds251819.mlab.com"
port = 51819
db_name = "project_earth_hero"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
