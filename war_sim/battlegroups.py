class Army_Element():
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.command = data_dict['command']
        self.sub_unit_elements = data_dict['sub_units']
        self.fire_support = data_dict['fire_support']
        self.attachments = data_dict['attachments']
        self.sub_unit_names = []

    def apply_casualties(self, casuality_dict):
        for unit_type, quantity in casuality_dict.items():
            for entry in self.command:
                if entry['name'] == unit_type:
                    entry['quantity'] = entry['quantity'] - quantity

    def summarize_units(self):
        totals = {}
        self.sub_unit_names = []
        for unit_type in self.command:
            if unit_type['name'] in totals:
                totals[unit_type['name']] += unit_type['quantity']
            else:
                totals[unit_type['name']] = unit_type['quantity']
        for unit_type in self.attachments:
            if unit_type['name'] in totals:
                totals[unit_type['name']] += unit_type['quantity']
            else:
                totals[unit_type['name']] = unit_type['quantity']
        for sub in self.sub_unit_elements:
            self.sub_unit_names.append(sub.name)
            for sub_name in sub.sub_unit_names:
                self.sub_unit_names.append(sub_name)
            for unit_type, quantity in sub.summarize_units().items():
                if unit_type in totals:
                    totals[unit_type] += quantity
                else:
                    totals[unit_type] = quantity
        return totals
    
    def summarize(self):
        return {self.name: {'unit_types': self.summarize_units(), 'sub_units': self.sub_unit_names}}


class Brigade(Army_Element):
    pass

class Battalion(Army_Element):
    pass

class Company(Army_Element):
    def __init__(self, data_dict):
        self.name = data_dict['name']
        self.command = data_dict['command']
        self.sub_unit_elements = []
        self.fire_support = []
        self.attachments = []
        self.sub_unit_names = []

