import socket
import os

def ft_client(host, port, filepath):
    host = str(host)
    port = int(port)
    filepath = str(filepath)
    filename = os.path.basename(filepath)
    dataformat = 'utf-8'
    size = 2048
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    with open(filepath, "r", encoding=dataformat) as f:
        data = f.read()
        client.send(filename.encode(dataformat))
        msg = client.recv(size).decode(dataformat)
        print(f"[*] Server: {msg}")
        client.send(data.encode(dataformat))
        msg = client.recv(size).decode(dataformat)
        print(f"[*] Server: {msg}")
    client.close()
    print('[*] Close connection')
    
if __name__ == '__main__':
    ft_client(os.sys.argv[1], os.sys.argv[2], os.sys.argv[3])