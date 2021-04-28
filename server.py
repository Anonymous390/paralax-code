import socket
print(socket.gethostbyname(socket.gethostname()))

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from time import time, strftime, localtime, sleep

HOST = "0.0.0.0"
PORT = 5050

def log_line(status, *lines):
    pre = "[" + strftime("%H:%M:%S", localtime()) + "] |" + status + "|"
    print(pre, *lines)

def receive_input():
    global loop
    while loop:
        temp = input()
        if temp == "close" or temp == "exit":
            log_line("S", "Closing connections:", *addresses)
            for connection in connections: connection.sendall(b"\n")
        if temp == "exit":
            loop = False
            exit()

def check_connection():
    while loop:
        for connection, address in zip(connections, addresses):
            try: connection.sendall(b"\b")
            except ConnectionResetError: delete(connection, address)
        sleep(0.2)

def delete(connection, address):
    log_line("S", address, "has left.")
    try: send(connection, usernames[address] + b" has left the chat room.")
    except KeyError: send(connection, str(address).encode() + b" has left the chat room.")
    del sent[connection]
    del muted[connection]
    try: del usernames[address]
    except: pass
    connections.remove(connection)
    addresses.remove(address)
    connection.close()

def check_socket(sock, addr):
    global sent, loop, usernames
    while loop:
        temp = b""
        while temp == b"":
            try: temp = sock.recv(1024)
            except: pass
        if temp != b"\a": log_line("M", addr, "sends " + repr(temp.decode()))
        if temp[:6] == b":user " and addr not in usernames:
            if temp[6:] not in usernames.values():
                sock.sendall(b"\a")
                usernames[addr] = temp[6:]
            else: sock.sendall(b"\r")
        elif temp == b"exit": delete(sock, addr)
        elif temp == b":list-people":
            text = b"\n".join((usernames[addr] for address in addresses))
            sock.sendall(text)
        elif temp[:6] == b":mute ":
            sock.sendall(f"This chat will be muted for {temp[6:].decode()} minute(s). You will not be able to retrieve muted messages.".encode())
            muted[sock] = float(temp[6:]) * 60
        elif temp == b":unmute":
            sock.sendall(b"You have been unmuted.")
            muted[sock] = 0
        elif temp == b":mute-status":
            sock.sendall(format_time(muted[sock]))
        elif temp != b"\a": sent[sock] = temp

def listen():
    global connections, addresses, sent
    while loop:
        s.listen()
        try: connection, address = s.accept()
        except: pass
        log_line("S", "Connected to", address)
        connections.append(connection)
        addresses.append(address)
        sent[connection] = b""
        muted[connection] = 0
        socket_check = Thread(target = check_socket, args = (connection, address))
        socket_check.start()

def send(conn, msg):
    for connection in connections:
        if connection != conn and muted[connection] == 0:
            connection.sendall(msg)

def format_time(seconds):
    if seconds != 0: string = "You are muted for "
    else: return "You are not muted. Mute yourself with the :mute command."
    if seconds // 3600 != 0: string += str(seconds // 3600) + " hours"
    string += " and " if seconds % 60 == 0 else ", "
    if seconds // 60 != 0: string += str(seconds // 60) + " minutes"
    if seconds % 60 != 0: string += str(seconds % 60)
    string += "."
    return string

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    log_line("S", "Server successfully started at", HOST, "Port:", PORT)
    connections = []
    addresses = []
    sent = {}
    muted = {}
    usernames = {}
    loop = True
    dt = time()
    listener = Thread(target = listen)
    connection_thread = Thread(target = check_connection)
    input_check = Thread(target = receive_input)
    listener.start()
    connection_thread.start()
    input_check.start()
    while loop:
        for connection, address in zip(connections, addresses):
            if sent[connection] != b"": send(connection, b"".join((usernames[address], b" sends ", repr(sent[connection].decode()).encode())))
            sent[connection] = b""
            try:
                if muted[connection] > 0:
                    muted[connection] -= time() - dt
                    if muted[connection] <= 0:
                        connection.sendall(b"You have been unmuted.")
                        muted[connection] = 0
            except KeyError: pass
            dt = time()