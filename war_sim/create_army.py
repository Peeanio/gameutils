import battlegroups
import random
import json
import couchdb

'''
generate battalion, british army 1980s, load into couchdb
'''

brits = {'tank': 'chieftein', 'transport': 'spartan', 'recce_light_vic': 'ferret', 'close_recce_vic': 'scorpion', 'at_vic': 'swingfire', 'heavy_at_vic': 'striker', 'inf_mortar': '81mm mortar', 'inf_light_mortar': '81mm mortar', 'inf_atgm': 'milan', 'inf_mmg': 'gpmg', 'recce_vic_medium': 'fox'}


def main():
    mech_inf_battalion_elements = []
    armoured_battalion_elements = []
    couch = couchdb.Server("http://admin:mysecretpassword@localhost:5984/")
#    company_db = couch.create('companies')
#    battalions_db = couch.create('battalions')
#    brigade_db = couch.create('brigades')
#    unit_types_db = couch.create('unit_types')

    for i in range(1,4):
        mech_company = battlegroups.Company({'name': (get_name("../nouns.txt").upper() + " Company"), 'command': [{'name': 'commander', 'quantity': 1}, {'name': 'infantry', 'quantity': 9}, {'name': brits['inf_mmg'], 'quantity': 1}, {'name': brits['inf_light_mortar'], 'quantity': 1}, {'name': brits['transport'], 'quantity': 6}]})
        mech_inf_battalion_elements.append(mech_company)
         
    close_recce_company = battlegroups.Company({'name': (get_name("../nouns.txt").upper() + " Company"), 'command': [{'name': brits['recce_vic_medium'], 'quantity': 4}]})

    mech_inf_battalion_elements.append(close_recce_company)

    guided_weapons_troop = battlegroups.Company({'name': (get_name("../nouns.txt").upper() + " Company"), 'command': [{'name': brits['recce_light_vic'], 'quantity': 1}, {'name': brits['at_vic'], 'quantity': 12}, {'name': brits['heavy_at_vic'], 'quantity': 4}]})

    armoured_battalion_elements.append(guided_weapons_troop)

    recce_company = battlegroups.Company({'name': (get_name("../nouns.txt").upper() + " Company"), 'command': [{'name': brits['close_recce_vic'], 'quantity': 4}]})

    armoured_battalion_elements.append(recce_company)

    for i in range(1,3):
        armoured_squadron = battlegroups.Company({'name': (get_name("../nouns.txt").upper() + " Company"),'command': [{'name': brits['tank'], 'quantity': 7}]})
        armoured_battalion_elements.append(armoured_squadron)

    for company in mech_inf_battalion_elements + armoured_battalion_elements:
        print(json.dumps(company.summarize()))
    #    company_db[company.name] = company.summarize()

    mech_infantry_battalion = battlegroups.Battalion({'name': "2nd Battalion",'command': [{'name': 'commander', 'quantity': 1}, {'name': brits['transport'], 'quantity': 1}], 'attachments': [{'name': brits['inf_mortar'], 'quantity': 4}, {'name': brits['transport'], 'quantity': 9}, {'name': brits['inf_atgm'], 'quantity': 8}], 'sub_units':  mech_inf_battalion_elements, 'fire_support': []})

    armoured_battalion = battlegroups.Battalion({'name': "1st Battalion", 'command': [{'name': brits['tank'], 'quantity': 1}, {'name': brits['recce_light_vic'], 'quantity': 1}], 'attachments': [], 'sub_units': armoured_battalion_elements, 'fire_support': []})

    print(json.dumps(mech_infantry_battalion.summarize()))
    
    print(json.dumps(armoured_battalion.summarize()))

    armoured_brigade = battlegroups.Brigade({'name': "1st Brigade", 'command': [{'name': brits['tank'], 'quantity': 1}, {'name': 'infantry', 'quantity': 3}, {'name': brits['transport'], 'quantity': 3}], 'attachments': [{'name': 'recon inf', 'quantity': 3}, {'name': brits['recce_light_vic'], 'quantity': 3}], 'sub_units': [armoured_battalion, mech_infantry_battalion], 'fire_support': []})

    print(json.dumps(armoured_brigade.summarize()))
    armoured_brigade.apply_casualties({brits['tank']: 1})
    print(json.dumps(armoured_brigade.summarize()))
    #print(json.dumps(armoured_brigade, default=lambda o: o.__dict__))

    

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
