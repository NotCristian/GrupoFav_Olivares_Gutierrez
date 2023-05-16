import socket
import threading

HEADER = 64
PORT = 3074
SERVER = '192.168.50.252'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    mac_received = False

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if not mac_received:
                if msg == '79:db:52:a3:ac:cc':
                    print(f"[{addr}] {msg}")
                    conn.send("MAC received".encode(FORMAT))
                    mac_received = True
                else:
                    connected = False
                    print("Error: MAC address doesn't match")
            else:
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    print('Device disconnected')
                    conn.send("Disconnected".encode(FORMAT))
                else:
                    print(f"[{addr}] {msg}")
                    conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTEN] Server is listening on address {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
start()
