# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import zmq
import json

context = zmq.Context()

request_data = {
    "dungeon_size": "large",
    "treasure_quality": "high_quality"
}

socket_server = context.socket(zmq.DEALER)
socket_client = context.socket(zmq.DEALER)

socket_server.bind("tcp://*:5555")

socket_client.connect("tcp://localhost:5556")

poller = zmq.Poller()

poller.register(socket_server, zmq.POLLIN)

socket_client.send_json(request_data)

while True:
    socks = dict(poller.poll())

    if socket_server in socks and socks[socket_server] == zmq.POLLIN:
        print("Received request")

    time.sleep(3)
    break

message = socket_server.recv()
treasure = json.loads(message)
print(f"Server sent back: {treasure}")

context.destroy()