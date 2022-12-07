#!/usr/bin/python3
#Author max@theguards.net

"""solo wargaming campaign-inspired creation tool"""

import argparse

parser = argparse.ArgumentParser(prog='campaign_creation_tool.py', \
description='multipurpose campaign creation utility')
subparsers = parser.add_subparsers(title='subcommands', description=\
'valid subcommands', help='campaign creation utility', \
dest='command_arg')
parser_map = subparsers.add_parser('map', help='campaign map creation')
args = parser.parse_args()

def generate_map():
    """generates the campaign map"""
    print("map")

if __name__ == '__main__':
    if args.command_arg == 'map':
        generate_map()
