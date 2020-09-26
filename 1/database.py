import time

class database:
    def __init__(self):
        print("Connecting to database...")
        time.sleep(3)
    def send(self, payload):
        print("Retreived connection")
        print("Sending " + payload)
        print(payload + " sent!")
    def retrieve(self, payload='payload'):
        print('Retrieved connection')
        print('Retrieveing '+payload)
        print('Result = '+payload)
