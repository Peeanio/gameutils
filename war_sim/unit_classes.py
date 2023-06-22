class MilitaryPerson():
    '''Personal details about a unit member'''
    
    def __init__(self, data_dict):
        self.rank = data_dict['rank']
        self.name = data_dict['name']
        self.weapons = data_dict['weapons']

class Weapon():
    '''Details about an individual weapon'''
    
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.capabilities = data_dict['capabilities']
        self.consumables = data_dict['consumables']

class Vehicle():
    '''Details about an individual vehicle'''

    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.capabilities = data_dict['capabilities']
        self.weapons = data_dict['weapons']
        self.consumables = data_dict['consumables']
        self.capacity = data_dict['capacity']

class Team():
    '''2-4 man unit, crew/patrol'''
    
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.unit_size = "Team"
        self.leader = data_dict['leader']
        self.members = data_dict['members']

class Squad():
    '''6-12 man unit'''
    
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.unit_size = "Squad"
        self.leader = data_dict['leader']
        self.teams = data_dict['members']

class Platoon():
    '''26-55 man unit, troop'''
    
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.unit_size = "Platoon"
        self.leader = data_dict['leader']
        self.attached = data_dict['attached']
        self.squads = data_dict['members']
