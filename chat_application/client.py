import socket
import time

# /Users/veresh/Desktop/Python/pyQt5/sock/client.py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(socket.gethostname()), 5050))

run = True


def receive():
    full_msg = ''
    msg = s.recv(1024)
    if len(msg) <= 0:
        run = False
    full_msg += msg.decode("utf-8")
    print(full_msg)


while run:
    time.sleep(0.1)

    with open('/Users/veresh/Desktop/Github/Coding/chat_application/turns.txt', 'r') as t:
        if t.read() == "client receive":
            receive()
    a = input("You: ")
    s.send(bytes(a, "utf-8"))
    with open('/Users/veresh/Desktop/Github/Coding/chat_application/turns.txt', 'w') as t:
        t.write('server receive')
