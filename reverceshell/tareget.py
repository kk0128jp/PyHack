import socket

def listener():
    # ホスト名 取得
    host = socket.gethostname()
    # ipアドレスを取得
    ip = socket.gethostbyname(host)
    # サーバーホスト、ポート
    server_host = ip
    server_port = 1234
    print("my ip is...", server_host)
    
    
    # 接続待ち
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    
    print("waiting for incoming connections.....")
    
    while True:
        # クライアントとの接続
        client_socket, client_address = server_socket.accept()
        print('Connected by', client_address)
        
        # データ受信
        data = client_socket.recv(1024).decode("utf-8")
        print("Get message is [", data, "]")
        
        # レスポンスの送信
        response = 'Hello, client!'
        client_socket.send(response.encode("utf-8"))
        
        # close
        client_socket.close()

if __name__ == '__main__':
    listener()