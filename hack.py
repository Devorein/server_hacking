import itertools
import sys
import socket

file = open('passwords.txt', 'r')
passwords = [x.strip('\n') for x in file]


def connecting_to_server():
    connection = socket.socket()
    argv = sys.argv
    host, port = '127.0.0.1', 9090
    connection.connect((host, port))
    for i in brutforce_password(passwords):
        password = i
        connection.send(password.encode())
        answer = connection.recv(1024)
        if answer.decode() == 'Connection success!':
            print("Correct password", password)
            break

    connection.close()


def brutforce_password(typical_passwords):
    for password in typical_passwords:
        passwords = map(''.join, itertools.product(
            *((c.upper(), c.lower()) for c in password)))
        for x in passwords:
            yield x


connecting_to_server()
