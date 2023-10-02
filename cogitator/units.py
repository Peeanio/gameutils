class Unit():
    '''Universal unit object'''
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.statline = data_dict['statline']
        self.unit_composition = data_dict['unit_composition']
        self.wargear = data_dict['wargear']
        self.unit_type = data_dict['unit_type']
        self.special_rules = data_dict['special_rules']
        self.options = data_dict['options']

class StatLine():
    '''Statline object'''
    def __init__(self, data_dict):
        self.
