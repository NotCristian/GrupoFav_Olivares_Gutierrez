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
    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length =int(msg_length)
    mac = conn.recv(msg_length).decode(FORMAT)
    print(mac)
    connected = True
    if mac=='79:db:52:a3:ac:cc':
        connected = True
        print('MAC address matched')
    else:
        connected = True
        print("Error MAC address doesn't match")
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        print('ACA')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

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

print("[STARTING] server is running.....")
start()
