from Backend.src.parser_generic import MedicalParser
import re

class PatientParser(MedicalParser):
    def __init__(self, text):
        MedicalParser.__init__(self, text)

    def parser(self):
        return {
            'name': self.get_field('name'),
            'address': self.get_field('address'),
            'phone_number': self.get_field('phone'),
            'vaccination': self.get_field('vaccination'),
            'medical_problems': self.get_field('medical_problems'),
        }

    def get_field(self, field_name):
        pattern_dict = {
            'name': {'pattern': r'Patient Information\s([^\n]+)', 'flag': re.DOTALL},
            'address': {'pattern': r'Patient Information\s[^\n]+\s\n[^\n]+\s[^\n]+\n(.*)In Case', 'flag': re.DOTALL},
            'phone': {'pattern': r'Patient Information\s[^\n]+\s\n([^\n]+)', 'flag': re.DOTALL},
            'vaccination': {'pattern': r'vaccination[^\n]\s*([^\n]+)', 'flag': re.DOTALL},
            'medical_problems': {'pattern': r'List any Medical Problems[^\n]*\s*([^\n]+)', 'flag': re.DOTALL}
        }
        get_object = pattern_dict.get(field_name)
        if get_object:
            text = re.findall(get_object['pattern'], self.text, get_object['flag'])
            return text[0].strip() if text else None