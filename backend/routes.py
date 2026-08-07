from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test():
    return {"cool" : "ok"}

######################### Websocket #################################

from fastapi import WebSocket, WebSocketDisconnect
from backend.agent import call_agent

@router.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_json()

            response = call_agent({
                "messages": [
                    {
                        "role": "user",
                        "content": data["message"]
                    }
                ]
            })

            await websocket.send_json({"content" : response})

    except WebSocketDisconnect:
        print("Client disconnected")
    