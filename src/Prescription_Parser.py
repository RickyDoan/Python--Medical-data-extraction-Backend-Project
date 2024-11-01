import re

from parser_generic import MedicalParser


class PrescriptionParser(MedicalParser):
    def __init__(self, text):
        MedicalParser.__init__(self, text)

    def parser(self):
        return {
            # 'name':self.get_name(),
            # 'address':self.get_address(),
            # 'description':self.get_description(),
            # 'direction':self.get_directions(),
            # 'refill':self.get_refill(),
         #------- Transfer from long call function to short call function below, but still keep everything ---#

            'name' :self.get_field('name'),
            'address' :self.get_field('address'),
            'description' :self.get_description(),
            'direction' :self.get_field('direction'),
            'refill' :self.get_field('refill'),
        }

    def get_field(self, field_name):
        pattern_dict={
            'name' : {'pattern' :'Name:(.*)Date', 'flags' :0 },
            'address' : {'pattern' :'Address:(.*)', 'flags' :0 },
            # 'description' : {'pattern' :'Address:\s[^\n]+\n+\s[^\n]\s(.*)Directions:', 'flags' :re.DOTALL },
            'direction' : {'pattern' :'Directions:(.*)Refill', 'flags' :re.DOTALL },
            'refill' : {'pattern' :'Refill:\s(.*)', 'flags' :0 },
        }
        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            match = re.findall(pattern_object['pattern'], self.text, pattern_object['flags'])
            if len(match) > 0:
                return match[0].strip()


    # def get_name(self):
    #     pattern = 'Name:(.*)Date'
    #     name = re.findall(pattern, self.text)
    #     return name[0].strip()
    #
    # def get_address(self):
    #     pattern = 'Address:(.*)'
    #     address = re.findall(pattern, self.text)
    #     return address[0].strip()
    #
    def get_description(self):
        pattern2 = 'Address[^\n]*(.*)Directions:'
        description2 = re.findall(pattern2, self.text, re.DOTALL)
        data = description2[0].strip()
        for i in data:
            if i == 'K':
                pattern4 = '\w*K\w*'
                new1 = re.findall(pattern4, data)
                new1 = new1[0].strip()
                new = data.replace(new1, '').strip()
                return new
            else:
                data
    #
    # def get_directions(self):
    #     pattern = 'Directions:\s*(.*?)\s*Refill:'
    #     match = re.findall(pattern, self.text, re.DOTALL)
    #     return match[0].strip()
    #
    # def get_refill(self):
    #     pattern = 'Refill:(.*times)'
    #     refill = re.findall(pattern, self.text)
    #     return refill[0].strip()

if __name__ == '__main__':
    document = '''
page 1:
 Dr John Smith, M.O
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Maria Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,

Finish in 2.5 weeks
Liatda - take 2 pill everyday for 1 month

Refill: 2. times

    '''
    pp = PrescriptionParser(document)
    print(pp.parser())