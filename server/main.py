from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "SCRYPT Monitor Online"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Aqui simulamos o envio de um preço para o teu React
            await websocket.send_json({"symbol": "BTCUSDT", "price": 65000.00})
            await asyncio.sleep(1)
    except Exception as e:
        print(f"Connection closed: {e}")