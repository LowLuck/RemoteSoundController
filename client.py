import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9090         # The port used by the server

sock = socket.socket()
sock.connect((HOST, PORT))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print('Received', repr(data))
