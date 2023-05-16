import socket
import uuid
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

def encrypt(plain_text):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted_bytes = cipher.encrypt(pad(plain_text.encode(FORMAT), AES.block_size))
    return encrypted_bytes

def decrypt(cipher_text):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted_bytes = unpad(cipher.decrypt(cipher_text), AES.block_size)
    return decrypted_bytes.decode(FORMAT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    encrypted_msg = encrypt(msg)
    msg_length = len(encrypted_msg)
    send_length = str(msg_length).encode(FORMAT)

    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(encrypted_msg)
    response = client.recv(2048)
    decrypted_response = decrypt(response)
    print(decrypted_response)

# Envío de la MAC
MAC = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)])
send(MAC)
send('hello')
send('asdfasdf')
send(DISCONNECT_MESSAGE)