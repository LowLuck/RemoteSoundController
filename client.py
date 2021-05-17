import socket
from Audiocontorller import AudiocontrollerCode

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9090  # The port used by the server
wordlist = ['up', 'down', 'half', 'full', 'mute', 'unmute', 'stop']

sock = socket.socket()
sock.connect((HOST, PORT))

Audiocontorller = AudiocontrollerCode()
Audiocontorller.main_start()


sock.send(bytes(Audiocontorller.get_process(),  encoding='utf-8'))
while True:
    message = input()
    if message in wordlist:
        sock.send(bytes(message, encoding='utf-8'))
        if message == 'stop':
            sock.send(b'stop')
            break
    else:
        print('Command not found')

sock.close()
