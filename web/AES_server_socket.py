import socket
import threading

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = b'Clavedeprueba123'
IV = b'InitializationVe'

HEADER = 64
PORT = 3074
SERVER = '192.168.50.252'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

def encrypt(plain_text):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode(FORMAT), AES.block_size))
    return encrypted_bytes

def decrypt(cipher_text):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted_bytes = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return decrypted_bytes.decode(FORMAT)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    mac_received = False

    while connected:
        msg_length = conn.recv(HEADER).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)

            if not mac_received:
                if decrypt(msg) == '79:db:52:a3:ac:cc':
                    print(f"[{addr}] {decrypt(msg)}")
                    conn.send(encrypt("MAC received"))
                    mac_received = True
                else:
                    connected = False
                    print("Error: MAC address doesn't match")
            else:
                if decrypt(msg) == DISCONNECT_MESSAGE:
                    connected = False
                    print('Device disconnected')
                    conn.send(encrypt("Disconnected"))
                else:
                    print(f"[{addr}] {decrypt(msg)}")
                    conn.send(encrypt("Msg received"))

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
