from parser_generic import MedicalParser
import re
#haha
class PatientParser(MedicalParser):
    def __init__(self,text):
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
            'name': {'pattern' : 'Information\s([^\n]+)', 'flag' : re.DOTALL},
            'address': {'pattern': 'Information\s[^\n]+\s*[^\n]+(.*)In Case', 'flag': re.DOTALL},
            'phone': {'pattern': 'Information\s[^\n]+\s*([^\n]+)', 'flag': re.DOTALL},
            'vaccination': {'pattern': 'vaccination.\s*([^\n]+)', 'flag': re.DOTALL},
            'medical_problems': {'pattern': 'Medical Problems[^\n]+\s*([^\n]+)', 'flag': re.DOTALL}
        }
        get_object = pattern_dict.get(field_name)
        if get_object:
            text = re.findall(get_object['pattern'], self.text, get_object['flag'])
            if len(text) > 0:
                return text[0].strip()



if __name__ == '__main__':
    document1 = '''
    page 1:
 Patient Medical Record

Patient Information
Jerry Lucas

(279) 920-8204
4218 Wheeler Ridge Dr

Buffalo, New York, 14201

United States

In Case of Emergency

Joe Lucas

Home phone

General Medical History

Chicken Pox (Varicelia):
IMMUNE

Have you had the Hepatitis B vaccination?

_ Yes

Birth Date
May 21998

Weight:
57

Height:
170

4218 Wheeler Ridge Dr
Buffalo, New York, 14201
United States

Work phone

Measles:

NOT IMMUNE

List any Medical Problems (asthma, seizures, headaches):

N/A.

17/12/2020
    '''
    data = PatientParser(document1).parser()
    print(data)