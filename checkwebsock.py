import json
import asyncio
import websockets

async def connect_to_websocket():
    url = "ws://127.0.0.1:8000/ws/notify-socket/?token=24c21dda66ec26516973dab3407cc87af1cc6e7a0ffe22866aa7a488a4377f18"

    async with websockets.connect(url) as websocket:
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            print("Data:", data)

            if data['type'] == 'chat':
                notification = ""
                for msg in data['messages']:
                    print(msg)
                    # Do something with the notification message

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_websocket())
