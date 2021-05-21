import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), 5050))
s.listen(5)


full_msg = ''
while True:
    clientsocket, address = s.accept()
    print(f"--> {address} has joined the chat!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    with open('/Users/veresh/Desktop/Python/pyQt5/sock/turns.txt', 'w') as t:
        t.write('client receive')
    while True:
        time.sleep(0.1)
        # Receive
        with open('/Users/veresh/Desktop/Python/pyQt5/sock/turns.txt', 'r') as t:
            if t.read() == 'server receive':
                msg = clientsocket.recv(1024)
                if len(msg) <= 0:
                    break
                full_msg += msg.decode("utf-8")
                # Send
                clientsocket.send(bytes(full_msg, "utf-8"))
                full_msg = ''
                with open('/Users/veresh/Desktop/Python/pyQt5/sock/turns.txt', 'w') as t:
                    t.write('client receive')

        # Close connection
        if full_msg == '!d':
            clientsocket.close()
            with open('/Users/veresh/Desktop/Python/pyQt5/sock/turns.txt', 'w') as t:
                t.write('')

