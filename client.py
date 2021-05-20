import socket
from Audiocontorller import AudiocontrollerCode

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9090  # The port used by the server
wordlist = ['up', 'down', 'half', 'full', 'mute', 'unmute']
onewordlist = ['half', 'full', 'mute', 'unmute']
textforuser = (f'\n'
               f'WARNING! Values are percentages of master volume! \n'
               f'1 -- sound equals to master, 0.5 half of main etc. \n'
               f'up <number> -- increase <percent> \n'
               f'down <number> --  decrease <percent> \n'
               f'half -- half of volume \n'
               f'full -- max volume \n'
               f'mute -- mute \n'
               f'unmute -- unmute \n'
               f'stop -- stop the program')

sock = socket.socket()
sock.connect((HOST, PORT))

Audiocontorller = AudiocontrollerCode()

processes = sock.recv(1024).decode("utf-8").split()

print('Processes in work (type refresh to refresh)')
print(processes)
print('Choose a process to work')

while True:
    w = input()
    if w in processes:
        sock.send(bytes(w, encoding='utf-8'))
        break
    elif w == 'refresh':
        sock.send(bytes('refr', encoding='utf-8'))
        processes = sock.recv(1024).decode("utf-8").split()
        print(processes)
    else:
        print('Process not found')
print(textforuser)

while True:
    message = input().split()
    if message[0] in wordlist:
        if message[0] in onewordlist:
            sock.send(bytes(message[0], encoding='utf-8'))
            print(sock.recv(1024).decode('utf-8'))
        elif message[0] not in onewordlist and len(message) == 2:
            if len(message[1]) != 1:
                if '.' in message[1]:
                    sock.send(bytes(' '.join(message), encoding='utf-8'))
                    print(sock.recv(1024).decode('utf-8'))
            else:
                sock.send(bytes(' '.join(message), encoding='utf-8'))
                print(sock.recv(1024).decode('utf-8'))
        else:
            print('Wrong format')
    elif message[0] == 'stop':
        sock.send(b'stop')
        break
    else:
        print('Command not found')

sock.close()
