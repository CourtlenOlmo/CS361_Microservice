# CS361_Microservice: Random Treasure Generator

## Communication Contract

Communication is done in this program using ZeroMQ's DEALER/DEALER biderectional pattern.

```
Port and Server Address for Main program:

Port: 5555

Server Address: tcp://<Server IP>:5556
```

```
Port and Server Address for Microservice program:

Port: 5556

Server Address: tcp://<Server IP>:5555
```

## Requesting Data

To request data, Main must send a dictionary named "request_data" containing the keys: dungeon_size, and treasure_quality.

dungeon_size must have one of three values: small, medium, large.

treasure_quality must be: low_quality, middle_quality, high_quality.

### Example Request

```
import zmq

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
```

## Receiving Data

Once the Microservice has received data, it will create a random number based on the size of the dungeon.

It will then loop through the chosen quality of treasure, choosing at random until the requested number has been selected.

It will then send the treasure back to the main program as a JSON file.

### Example Receive
```
context = zmq.Context()

socket_server = context.socket(zmq.DEALER)
socket_client = context.socket(zmq.DEALER)

socket_server.bind("tcp://*:5556")
socket_client.connect("tcp://localhost:5555")

poller = zmq.Poller()
poller.register(socket_server, zmq.POLLIN)

request = socket_server.recv()
treasureRequest = json.loads(request)
```
