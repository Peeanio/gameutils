#!/usr/bin/python3
#Author max@theguards.net

"""solo wargaming campaign-inspired creation tool"""

import argparse
import os
import random
import requests

parser = argparse.ArgumentParser(prog='campaign_creation_tool.py', \
description='multipurpose campaign creation utility')
subparsers = parser.add_subparsers(title='subcommands', description=\
'valid subcommands', help='campaign creation utility', \
dest='command_arg')
parser_map = subparsers.add_parser('map', help='campaign map creation')
args = parser.parse_args()

def generate_map():
    """generates the campaign map"""
    if os.path.exists('map.png'):
        print('file exists')
    else:
        max_x = 15
        max_y = 15
        grid_type = "hex"
        seed = random.randint(100000000, 999999999)
        payload = {"more": 0, "maxx": max_x, "maxy": max_y, "type": grid_type, "seed": seed}
        resp = requests.get('https://tools.dehumanizer.com/mapgen/map.php', \
        params=payload, stream=True, timeout=10)
        if resp.ok:
            with open('map.png', 'wb') as new_file:
                new_file.write(resp.content)
                print('file written')

if __name__ == '__main__':
    if args.command_arg == 'map':
        generate_map()
    else:
        parser.print_help()
