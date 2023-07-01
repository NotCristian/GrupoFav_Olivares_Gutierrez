import asyncio
import websockets
import csv
import socket

IP = '192.168.27.252'
PORT = 3074

async def send_csv_data(websocket, path):
    try:
        with open('datos.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                await websocket.send(','.join(row))
    finally:
        await websocket.close()

async def start_server():
    server = await websockets.serve(send_csv_data, IP, PORT)
    print(f"El servidor se encuentra funcionando y escuchando en la IP {IP}")
    await server.wait_closed()

try:
    asyncio.get_event_loop().run_until_complete(start_server())
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Interrupción del teclado detectada. Cerrando el servidor.")
