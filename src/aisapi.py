import asyncio
import websockets
import json
from datetime import datetime, timezone
#from main import
import requests
async def connect_ais_stream():
    try:
        async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
            subscribe_message = {"APIKey": "31f6f62533921cb9fdc90fd301da90f86a784eaa", "BoundingBoxes": [[[-90, -180], [90, 180]]]}

            subscribe_message_json = json.dumps(subscribe_message)
            await websocket.send(subscribe_message_json)

            async for message_json in websocket:
                message = json.loads(message_json)
                message_type = message["MessageType"]

                if message_type == "PositionReport":
                # the message parameter contains a key of the message type which contains the message itself
                    ais_message = message['Message']['PositionReport']
                    print(f"[{datetime.now(timezone.utc)}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Longitude: {ais_message['Longitude']}  Bearing: {ais_message['TrueHeading']}")
    except:
        return "Failed to Connect websocket."



async def call_staticshipdata(ShipId):
#*** review code and 
    # Set up API endpoint and parameters
    #api_endpoint = "wss://stream.aisstream.io/v0/stream"
    # Replace with the MMSI number of the ship you want to retrieve data for
    try:
        async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
            subscribe_message = {"APIKey": "31f6f62533921cb9fdc90fd301da90f86a784eaa", "BoundingBoxes": [[[-90, -180], [90, 180]]]}

            subscribe_message_json = json.dumps(subscribe_message)
            await websocket.send(subscribe_message_json)

            async for message_json in websocket:
                message = json.loads(message_json)
                message_UserId = message["UserId"]
    
                if message_UserId == dfsdf:
                    ais_message = message['Message']['ShipStaticData']
                    print(f"[{datetime.now(timezone.utc)}] CallSign: {ais_message['CallSign']} Name: {ais_message['Name']} Type: {ais_message['Type']}")
   
    except:
        return "Failed to Connect websocket"

if __name__ == "__main__":
    #asyncio.run(asyncio.run(connect_ais_stream()))
    asyncio.run(asyncio.run(call_staticshipdata(257069200)))
