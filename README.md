# CS361_Microservice: Random Treasure Generator

Communication is done in this program using ZeroMQ's DEALER/DEALER biderectional pattern.

Port and Server Address for Main program:

Port: 5555

Server Address: tcp://<Server IP>:5556

Port and Server Address for Microservice program:

Port: 5556

Server Address: tcp://<Server IP>:5555

---------------------------------------------------------------------------------------------
#Requesting Data

To request data, Main must send a dictionary named "request_data" containing the keys: dungeon_size, and treasure_quality.

dungeon_size must have one of three values: small, medium, large.

treasure_quality must be: low_quality, middle_quality, high_quality.

----------------------------------------------------------------------------------------------

#receiving data

Once the Microservice has received data, it will create a random number based on the size of the dungeon.

It will then loop through the chosen quality of treasure, choosing at random until the requested number has been chosen.

It will then send the treasure back to the main program as a JSON file.
