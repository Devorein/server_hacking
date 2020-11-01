import random
import socket
from string import ascii_lowercase, digits


HOST = '127.0.0.1'
PORT = 50003
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
    sckt.bind((HOST, PORT))
    sckt.listen(1)
    conn, addr = sckt.accept()
    password = 'BraZIL'
    with conn:
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if len(data) > 1_000_000:
                conn.send('Too many attempts to connect!'.encode('utf8'))
                break
            if not data:
                break
            if data.decode('utf8') == password:
                conn.send('Connection success!'.encode('utf8'))
            else:
                conn.send('Wrong password!'.encode('utf8'))