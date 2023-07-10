import socket

def client(target_ip):
    # 通信先サーバー
    server_host = target_ip
    server_port = 1234
    
    while True:
        # サーバーに接続
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host, server_port))
        
        # メッセージ送信
        message = input("Enter message:")
        client_socket.send(message.encode("utf-8"))
        print('Send Message')
        
        # サーバーからのレスポンス受信
        responce = client_socket.recv(1024).decode("utf-8")
        print('Server response:', responce)
        
        # close
        client_socket.close()

if __name__ == '__main__':
    client()