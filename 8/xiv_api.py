import json, requests

def get_fc_data():
    r = requests.get("https://xivapi.com/freecompany/9228438586435663178")
    return r.text

def get_fc_members():
    r = requests.get("https://xivapi.com/freecompany/9228438586435663178?data=FCM")
    return r.text

print(get_fc_members())
