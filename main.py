import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)  # maximum amount of connections
conn, addr = sock.accept()
print('connected:', addr)

fulldata = []
while True:
    data = conn.recv(1024)
    fulldata.append(data)
    if not data:
        break
    conn.send(data)
print(f'Recieved data: {fulldata}')
conn.close()
