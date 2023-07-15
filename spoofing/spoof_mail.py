import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import yaml

def sendMail(target_address):
    try:
        # 設定ファイル読み込み
        with open('setting.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)
    except Exception as e:
        print(e)
        print("[+] Can not load setting.yaml")
    # 送信元アドレス
    sender_email = config['sender_email']
    sender_pass = config['sender_pass']
    # 宛先アドレス
    target_email = target_address
    # メールサーバー
    smtp_host = config['smtp_host']
    smtp_port = config['smtp_port']
    
    # メール作成
    message = MIMEMultipart()
    message["Form"] = sender_email
    message["To"] = target_email
    message["Subject"] = "メールの件名"
    
    # メール本文作成
    body = "メールの本文です。"
    message.attach(MIMEText(body, "plain"))
    
    attachment_path = config['email_attach_path']
    attachment_filename = config['email_attach_file_name']
    
    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read())
        attachment.add_header('Content-Disposition', 'attachment', filename=attachment_filename)
        message.attach(attachment)
    
    try:
        # SMTPサーバーへの接続と送信
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            # TLS暗号化
            server.starttls()
            # SMTPサーバーへのログイン
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, target_email, message.as_string())
        print('[+] Email sent successfully.')
    except Exception as e:
        print("[+] Can not send email")