import socket
from Audiocontorller import AudiocontrollerCode

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9090  # The port used by the server
wordlist = ['up', 'down', 'half', 'full', 'mute', 'unmute']

sock = socket.socket()
sock.connect((HOST, PORT))

Audiocontorller = AudiocontrollerCode()
Audiocontorller.main_start()


processes = sock.recv(1024).decode("utf-8")
sock.send(bytes(Audiocontorller.get_process(),  encoding='utf-8'))
while True:
    message = input()
    if message in wordlist:
        sock.send(bytes(message, encoding='utf-8'))
    elif message == 'stop':
        sock.send(b'stop')
        break
    else:
        print('Command not found')

sock.close()
