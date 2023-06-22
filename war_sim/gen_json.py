import unit_classes
import json
import random


'''
generate json docs for units
'''

rifle = unit_classes.Weapon({'name': 'L1A1', 'capabilities': 'direct-fire', 'consumables': '7.62mm'})
pistol = unit_classes.Weapon({'name': 'Browning HiPower', 'capabilities': 'direct-fire', 'consumables': '9mm'})
sub_gun = unit_classes.Weapon({'name': 'Sterling', 'capabilities': 'direct-fire', 'consumables': '9mm'})
grenade_launcher = unit_classes.Weapon({'name': 'Energa Rifle Grenade', 'capabilities': ['direct-fire', 'indirect-fire'], 'consumables': 'rifle grenade'})
light_machine_gun = unit_classes.Weapon({'name': 'Bren', 'capabilities': ['direct-fire', 'supressing-fire'], 'consumables': '7.7mm'})
medium_machine_gun = unit_classes.Weapon({'name': 'L7', 'capabilities': ['direct-fire', 'supressing-fire'], 'consumables': '7.62mm'})
medium_at = unit_classes.Weapon({'name': 'Carl-Gustav', 'capabilities': ['direct-fire', 'anti-tank'], 'consumables': '84mm'})
light_at = unit_classes.Weapon({'name': 'M72', 'capabilities': ['direct-fire', 'anti-tank', 'high-explosive'], 'consumables': '66mm'})
light_mortar = unit_classes.Weapon({'name': 'Mortar', 'capabilities': ['supressing-fire', 'indirect-fire'], 'consumables': '81mm'})
transport = unit_classes.Vehicle({'name': "FV432", 'capabilities': ['tracked', 'transport'], 'weapons': medium_machine_gun, 'capacity': 10, 'consumables': ['diesel']})
rank_list = ["Private", 'Lance Corporal', "Corporal", "Sergent", "Lieutenant"]

def main():
    print(json.dumps(generate_unit_platoon(get_name("../nouns.txt").upper(), []), default=lambda o: o.__dict__))

def generate_military_person(rank):
    '''generates a MilitaryPerson object with rank input'''
    data_dict = {}
    data_dict['rank'] = rank
    data_dict['weapons'] = [rifle]
    if rank == rank_list[1]:
        data_dict['weapons'].append(grenade_launcher)
    elif rank == rank_list[2] or rank == rank_list[3]:
        data_dict['weapons'].append(pistol)
    elif rank == rank_list[4]:
        data_dict['weapons'] = [sub_gun]
    data_dict['name'] = get_name("../firstnames.txt") + " " + get_name("../surnames.txt")
    return unit_classes.MilitaryPerson(data_dict)

def generate_unit_team(name):
    '''generates a Team unit'''
    member_list = []
    for i in range(1, 6):
        if i == 1:
            person = generate_military_person(rank_list[1])
        else:
            person = generate_military_person(rank_list[0])
        if i == 4:
            person.weapons.append(light_machine_gun)
        if i == 5:
            person.weapons.append(light_at)
        member_list.append(person)
    leader = member_list[0]
    return unit_classes.Team({"name": name, 'members': member_list, "leader": leader})

def generate_unit_squad(name):
    '''generates a Squad unit with children'''
    member_list = []
    for i in range(1, 3):
        member_list.append(generate_unit_team(name + "-" + str(i)))
    leader = generate_military_person(rank_list[2])
    return unit_classes.Squad({"name": name, 'members': member_list, "leader": leader})

def generate_unit_platoon(name, attached):
    '''generates a Platoon unit with children'''
    member_list = []
    for i in range(1, 3):
        member_list.append(generate_unit_squad(name + "-" + str(i)))
    leader = generate_military_person(rank_list[4])
    support = [generate_unit_weapon_team(name + "-" + str(3), light_mortar), generate_unit_weapon_team(name + "-" + str(4), medium_at)]
    vehicles = {"quantity": 6, "type": transport}
    attached = {'support': support, 'vehicles': vehicles}
    return unit_classes.Platoon({"name": name, 'members': member_list, "leader": leader, "attached": attached})

def generate_unit_weapon_team(name, weapon):
    '''gnerates a Team with heavier weapon'''
    member_list = []
    for i in range(1, 4):
        if i == 1:
            person = generate_military_person(rank_list[1])
        else:
            person = generate_military_person(rank_list[0])
            person.weapons.append(weapon)
        member_list.append(person)
    leader = member_list[0]
    return unit_classes.Team({"name": name, 'members': member_list, "leader": leader})

def file_len(file_name):
    '''open the file, count the lines, return'''
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_name(file_name):
    '''function to get content from a line in file'''
    num_of_lines = file_len(file_name)
    random_num = random.randint(0, num_of_lines)
    file = open(file_name)
    all_lines = file.readlines()
    return str(all_lines[random_num].strip())

if __name__ == '__main__':
    main()
