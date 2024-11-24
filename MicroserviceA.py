import zmq
import json
import random

context = zmq.Context()

quality_map = {
    "low_quality": {
        "Weapons": ["copper sword", "wooden sword", "unstrung bow"],
        "Potions": ["low quality potion", "half full mana potion"],
        "Enchanted Items": ["Ring of fast walking", "Brooch of minor strength", "Socks of sweat removal"],
        "Food": ["moldy cheese", "old milk", "old bone", "jar of honey"],
        "Currency": ["10 copper coins", "25 copper coins", "50 copper coins"]
    },
    "medium_quality": {
        "Weapons": ["iron sword", "longbow", "steel axe"],
        "Potions": ["medium quality potion", "stamina potion"],
        "Enchanted Items": ["Amulet of quickness", "Charm of moderate strength", "Boots of speed"],
        "Food": ["aged cheese", "fresh bread", "smoked fish"],
        "Currency": ["10 silver coins", "25 silver coins", "50 silver coins"]
    },
    "high_quality": {
        "Weapons": ["golden sword", "enchanted bow", "mythical axe"],
        "Potions": ["high quality potion", "elixir of vitality"],
        "Enchanted Items": ["Cloak of invisibility", "Ring of immense strength", "Orb of power"],
        "Food": ["feast platter", "royal wine", "mystical fruit"],
        "Currency": ["10 gold coins", "25 gold coins", "50 gold coins"]
    }
}

returnJson = {
    "Treasure" : {
    }
}

print("Client attempting to connect to server...")

socket_server = context.socket(zmq.DEALER)
socket_client = context.socket(zmq.DEALER)

socket_server.bind("tcp://*:5556")
socket_client.connect("tcp://localhost:5555")

poller = zmq.Poller()

poller.register(socket_server, zmq.POLLIN)



#get request from main
request = socket_server.recv()
treasureRequest = json.loads(request)
size = treasureRequest["dungeon_size"]
quality = treasureRequest["treasure_quality"]


print(f"Request Received. Dungeon size: {size}  Dungeon Quality: {quality}")

#Establish the size of the dungeon
if size == "small":
    treasureAmount = random.randrange(2,4)
elif size == "medium":
    treasureAmount = random.randrange(4, 7)
elif size == "large":
    treasureAmount = random.randrange(7, 10)

#Establish the quality of dungeon
if quality == "low_quality":
    quality = low_quality
elif quality == "middle_quality":
    quality = medium_quality
elif quality == "high_quality":
    quality = high_quality

#Loop through chosen quality dictionary, adding to JSON dict until "treasureAmount" been reached
for i in range(treasureAmount):
    treasureType = random.choice(list(quality.keys()))
    treasureItem = random.choice(list(quality[treasureType]))
    update = {treasureType : treasureItem}
    if treasureType in returnJson["Treasure"]:
        if isinstance(returnJson["Treasure"][treasureType], list):
            overlap = returnJson["Treasure"][treasureType]
        else:
            overlap = [(returnJson["Treasure"][treasureType])]
        overlap.append(update[treasureType])
        update = {treasureType : overlap}
        returnJson["Treasure"].update(update)
    else:
        returnJson["Treasure"].update(update)

returnJson = json.dumps(returnJson)

socket_client.send_json(returnJson)
socket_client.send_string("Q")
