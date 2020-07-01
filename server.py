import socket
import random
import binascii


def client_manager(conn, addr):
    file_size = conn.recv(1024).decode()
    print(file_size)
    data = conn.recv(int(file_size)).decode()
    try:
        randNum = random.randint(0, 100)
        filename = "image"+str(randNum)+".jpg"
        with open(filename , "wb") as f:
            f.write(binascii.unhexlify(data))
        print("created new image file.")
    except:
        print("Unable to print new image")

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("127.0.0.1", 50000))
socket.listen()
while 1:
    conn, addr = socket.accept()
    client_manager(conn, addr)
