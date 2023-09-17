import socket

def ft_server(host, port):
    host = str(host)
    port = int(port)
    dataformat = 'utf-8'
    size = 2048
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    
    while True:
        print(f"[*] Listening {host}:{port}...")
        try:
            conn, address = server.accept()
            print(f"[*] Connetcting {address}....")
            filename = conn.recv(size).decode(dataformat)
            with open(filename, 'w', encoding=dataformat) as f:
                conn.send(f"{filename} Received.".encode(dataformat))
                data = conn.recv(size).decode(dataformat)
                print(f"[*] Receiving the file data.")
                f.write(data)
                conn.send("[*] File data receive".encode(dataformat))
            conn.close()
            print('[*] Close connection.')
            print("[*] Continue Accept.")
            continue
        except Exception as e:
            print(f"[*]Error: {e}")
            print("[*] Continue Accept.")
            continue