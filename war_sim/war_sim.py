import battlegroups
import random
import json
import couchdb
import logging
import argparse
import yaml

parser = argparse.ArgumentParser(prog='war_sim.py', description='database-backed war simulator')
subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands', help='war sim commands', dest='subcommand')
parser_load_db = subparsers.add_parser('load_db', help='load database from config file')
parser_load_db.add_argument("-c", dest="config", help="path of config file, default ~/.war_sim.conf", default="~/.war_sim.conf")
args = parser.parse_args()

def main():
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  all_config = parse_config(args.config)
  match args.subcommand:
    case "load_db":
      load_db(all_config)

def load_db(all_config):
  server = all_config['server']
  address = "http://" + server['db_username'] + ":" + server['db_password'] + '@'+ server['db_address'] + ":" + str(server['db_port']) + "/"
  logging.info(address)
  couch = couchdb.Server(address)
  try:
    db = couch['unit_types']
  except Exception as err:
    logging.info(err)
    db = couch.create('unit_types')
  for army in all_config['armies']:
#    logging.info(all_config['armies'][army])
    doc = db.save(dict(all_config['armies'][army]['types']))


def get_army():
  pass

def parse_config(config_path):
  with open(config_path, 'r') as conf_contents:
    data = yaml.load(conf_contents, Loader=yaml.SafeLoader)
    return data

# main
if __name__ == '__main__':
  if args.subcommand is not None:
    main()
  else:
    parser.print_help()
