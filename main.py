import socket
from Audiocontorller import AudiocontrollerCode
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)  # maximum amount of connections
conn, addr = sock.accept()
print('connected:', addr)

fulldata = []
Class = AudiocontrollerCode()
status = True
prevdata = ''

data = conn.recv(1024).decode("utf-8")
if not Class.get_process():
    Class.set_process(data)

while True:
    data = conn.recv(1024).decode("utf-8")  # decoding data
    print(data)
    fulldata.append(data)

    if data != 'Emp':
        Class.serverwork(data)

    if not data:
        break

    data = 'Emp'
    time.sleep(3)

print(f'Recieved data: {fulldata}')
conn.close()
