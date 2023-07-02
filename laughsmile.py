from scapy.all import IP, TCP, send
from faker import Faker

# 引数から宛先IPの受け取り
get_dst_ip = ''

# 偽IPv4アドレスを生成
fake = Faker()
src_ip = fake.ipv4()

src_dst_ip = IP(src_ip, get_dst_ip)
send()
# TCP packet
#https://xtech.nikkei.com/atcl/nxt/column/18/00975/091700008/

#Python option
#https://qiita.com/Esfahan/items/72b3c34d744eaaea6c93