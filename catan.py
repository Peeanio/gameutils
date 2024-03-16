import random
import json

# tiles = [{"cord":(-1, -2)}, {"cord":(0, -2)}, {"cord":(1, -2)},
#          {"cord":(-1, -1)}, {"cord":(0, -1)}, {"cord":(1, -1)}, {"cord":(2, -1)},
#          {"cord":(0, -2)}, {"cord":(0, -1)}, {"cord":(0, 0)}, {"cord":(0, 1)}, {"cord":(0, 2)},
#          {"cord":(-1, 1)}, {"cord":(0, 1)}, {"cord":(1, 1)}, {"cord":(2, 1)},
#          {"cord":(-1, 2)}, {"cord":(0, 2)}, {"cord":(1, 2)}]

tile_types = ["brick", "brick", "brick", "ore", "ore", "ore", "wheat", "wheat", "wheat", "wheat", "wood", "wood", "wood", "wood", "sheep", "sheep", "sheep", "sheep", "desert"]
tile_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

shore_tiles = [[{"type": "none", "amount": 0}, {"type": "any", "amount": 3}, {"type": "none", "amount": 0}], [{"type": "any", "amount": 3}, {"type": "none", "amount": 0}, {"type": "brick", "amount": 2}], [{"type": "none", "amount": 0}, {"type": "wood", "amount": 2}, {"type": "none", "amount": 0}], [{"type": "wheat", "amount": 2}, {"type": "none", "amount": 0}, {"type": "any", "amount": 3}], [{"type": "none", "amount": 0}, {"type": "ore", "amount": 2}, {"type": "none", "amount": 0}], [{"type": "sheep", "amount": 2}, {"type": "none", "amount": 0}, {"type": "any", "amount": 3}]]

tiles = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

shore_placement = ['','','','','','']

for tile in tiles:
    type_remaining = len(tile_types)
    number_remaining = len(tile_numbers)
    # print(length_remaining)
    sel_type = random.randint(0, type_remaining)
    sel_num = random.randint(0, number_remaining)
    # print(selected)
    if sel_type == type_remaining:
        sel_type = sel_type -1
    if sel_num == number_remaining:
        sel_num = sel_num -1
    tile["type"] = tile_types.pop(sel_type)
    if tile["type"] == "desert":
        tile["number"] = 7
        continue
    tile["number"] = tile_numbers.pop(sel_num)
# print(tiles)

for i, shore in enumerate(shore_placement):
    shore_remaining = len(shore_tiles)
    sel_shore = random.randint(0, shore_remaining)
    if sel_shore == shore_remaining:
        sel_shore = sel_shore -1
    shore_placement[i] = shore_tiles.pop(sel_shore)

# for tile in tiles:
#     if tile['type'] == "desert":
#         print(tile)

# print(shore_placement)


# print(json.dumps([shore_placement[0][0], shore_placement[0][1], shore_placement[0][2], shore_placement[1][0]]))
# print(json.dumps([shore_placement[5][2], tiles[0], tiles[1], tiles[2], shore_placement[1][1]]))
# print(json.dumps([shore_placement[5][1], tiles[3], tiles[4], tiles[5], tiles[6], shore_placement[1][2]]))
# print(json.dumps([shore_placement[5][0], tiles[7], tiles[8], tiles[9], tiles[10], tiles[11], shore_placement[2][0]]))
# print(json.dumps([shore_placement[4][2], tiles[12], tiles[13], tiles[14], tiles[15], shore_placement[2][1]]))
# print(json.dumps([shore_placement[4][1], tiles[16], tiles[17], tiles[18], shore_placement[2][0]]))
# print(json.dumps([shore_placement[4][0], shore_placement[3][0], shore_placement[3][1], shore_placement[3][2]]))

rows = []
row_print = []

rows.append(([shore_placement[0][0], shore_placement[0][1], shore_placement[0][2], shore_placement[1][0]]))
rows.append(([shore_placement[5][2], tiles[0], tiles[1], tiles[2], shore_placement[1][1]]))
rows.append(([shore_placement[5][1], tiles[3], tiles[4], tiles[5], tiles[6], shore_placement[1][2]]))
rows.append(([shore_placement[5][0], tiles[7], tiles[8], tiles[9], tiles[10], tiles[11], shore_placement[2][0]]))
rows.append(([shore_placement[4][2], tiles[12], tiles[13], tiles[14], tiles[15], shore_placement[2][1]]))
rows.append(([shore_placement[4][1], tiles[16], tiles[17], tiles[18], shore_placement[2][0]]))
rows.append(([shore_placement[4][0], shore_placement[3][0], shore_placement[3][1], shore_placement[3][2]]))

# print(rows)
for i, row in enumerate(rows):
    if i == 0 or i == 6:
        print("   ", end="")
    elif i == 1 or i == 5:
        print("  ", end="")
    elif i == 2 or i == 4:
        print(" ", end="")
    for tile in row:
        if "amount" in tile:
            if tile["amount"] == 0:
                #sea
                print("_", end =" ")
            elif tile["amount"] > 0:
                if tile["type"] == "ore":
                    print("O", end =" ")
                elif tile["type"] == "brick":
                    print("B", end =" ")
                elif tile["type"] == "sheep":
                    print("S", end =" ")
                elif tile["type"] == "any":
                    print("?", end =" ")
                elif tile["type"] == "wood":
                    print("L", end =" ")
                elif tile["type"] == "wheat":
                    print("W", end =" ")
        else:
            if tile["type"] == "ore":
                print("O" + str(tile["number"]), end =" ")
            elif tile["type"] == "brick":
                print("B"+ str(tile["number"]), end =" ")
            elif tile["type"] == "sheep":
                print("S"+ str(tile["number"]), end =" ")
            elif tile["type"] == "any":
                print("?"+ str(tile["number"]), end =" ")
            elif tile["type"] == "wood":
                print("L"+ str(tile["number"]), end =" ")
            elif tile["type"] == "wheat":
                print("W"+ str(tile["number"]), end =" ")

    print()

