import battlegroups
import random
import json
import couchdb
import configparser
import argparse

parser = argparse.ArgumentParser(prog='war_sim.py', description='database-backed war simulator')
subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='war sim commands', dest='subcommand')
parser_load_db = subparsers.add_parser('load_db', help='load database from config file')
parser_load_db.add_argument("-c", dest="config", help="path of config file, default ~/.war_sim.conf", default="~/.war_sim.conf")
args = parser.parse_args()

def main():
 pass 

# main
if __name__ == '__main__':
  if args.subcommand is not None:
    main()
  else:
    parser.print_help()
