import json
import asyncio
import websockets

async def test(message):
    async with websockets.connect("ws://127.0.0.1:8000/chat") as ws:
        await ws.send(json.dumps({
            "message" : message
        }))
        print(await ws.recv())

async def multiple_users():
    await asyncio.gather(test("Hey man, whats up! post this: Stuff."))

asyncio.run(multiple_users())