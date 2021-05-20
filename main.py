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

q = Class.sys_clear(Class.process_get()[1])
conn.send(bytes(' '.join(q), encoding='utf-8'))

while True:
    data = conn.recv(1024).decode("utf-8")
    if data == 'refr':
        q = Class.sys_clear(Class.process_get()[1])
        conn.send(bytes(' '.join(q), encoding='utf-8'))
    else:
        break

if not Class.get_process():
    Class.set_process(data)
    print(Class.get_process())

while True:
    data = conn.recv(1024).decode("utf-8")  # decoding data
    fulldata.append(data)

    if data == 'stop':
        break

    if data != 'Emp':
        senddat = Class.serverwork(data)
        conn.send(bytes(senddat, encoding='utf-8'))

    if data == 'stop':
        break

    fulldata.append(data)


print(f'Recieved data: {fulldata}')
conn.close()
