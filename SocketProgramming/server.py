import socket
import threading

HEADER = 64 # 64 byte message size
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
# print("hostname: "+ str(socket.gethostname()))
# print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    '''Handle indvidual client runs concurrently'''
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #blocking line of code as it waits till we recieve the message from the client
        print(msg_length)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] : {msg}")

def start():
    '''
    This is the main thread that runs we are using -1 in threading.activeCount() - 1
    '''
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
