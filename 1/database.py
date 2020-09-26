import time

def send(payload):
    print("Connecting to database...")
    time.sleep(3)
    print("Retreived connection")
    print("Sending " + payload)
    print(payload + " sent!")
