import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import yaml

def sendMail(target_address):
    # 設定ファイル読み込み
    with open('../setting.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    # 送信元アドレス
    sender_email = config['sender_email']
    sender_pass = config['sender_pass']
    # 宛先アドレス
    receiver_email = target_address
    # メールサーバー
    smtp_host = config['smtp_host']
    smtp_port = config['smtp_port']
    
    # メール作成
    message = MIMEMultipart()
    message["Form"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "メールの件名"
    
    # メール本文作成
    body = "メールの本文です。"
    message.attach(MIMEText(body, "plain"))
    
    # SMTPサーバーへの接続と送信
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        # TLS暗号化
        server.starttls()
        # SMTPサーバーへのログイン
        server.login(sender_email, sender_pass)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email sent successfully.')
sendMail("aaafuta7@gmail.com")
        