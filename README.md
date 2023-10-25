# gameutils

This is a project is a collection of utilities for various board and tabletop games.

## chargen.py
First is a random character generator for pen and paper RPGs. It is a work in progress. Format is not stabalised, but the aim to is to create JSON blocks that are tailored for each game. Having a single program with pluggable game modules that define in a config file how to make a character for each game.

Games desired:
- Cyberpunk 2020 v2
- Dungeons and Dragons 5th Edition
- OSE (Old School Essentials)

## frostgrave.py
Second is a warband generator for the game Frostgrave. I wrote a test version in Go first, but did not think the project warranted that language, so it has been rewritten in Python. The GO version has been removed but can be found in git history.

## roll.py
A dice rolling utility that rolls any size or number of dice, or can be used to automatically do the math and return a final value for D&D 5e checks.

## tables.py
Given a file, take a random line and return the contents, ala rolling on a table.

## codename.py
Creates random operation or agent codenames, with some fun options

## campaign_creation_tool.py
A tool that can be used to create the basis of some type of tabletop or war campaign. As of now creates a png map with terrain types on a hex grid.


