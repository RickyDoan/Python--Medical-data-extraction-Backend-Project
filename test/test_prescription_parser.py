from fontTools.misc.cython import returns

from Backend.src.Prescription_Parser import PrescriptionParser
import pytest

path = '../resources/prescription/pre_2.pdf'

@pytest.fixture
def get_document1():
    document1 = '''
        Dr John Smith, M.D
        2 Non-Important Street,
        New York, Phone (000)-111-2222
        
        Name: Maria Sharapova Date: 9/11/2022
        
        Address: 9 tennis court, new Russia, DC
        
        
        
        Prednisone 20 mg
        Lialda 2.4 gram
        
        Directions:
        
        Prednisone, Taper 5 mg every 3 days,
        Finish in 2.5 weeks a
        
        Lialda - take 2 pill everyday for 1 month
        
        Refill: 2 times
        '''

    return PrescriptionParser(document1)

@pytest.fixture
def get_empty():
    return PrescriptionParser('')

def test_get_name(get_document1, get_empty):
    assert get_document1.get_field('name') == 'Maria Sharapova'
    assert get_empty.get_field('name') is None

def test_get_address(get_document1, get_empty):
    assert get_document1.get_field('address') == '9 tennis court, new Russia, DC'
    assert get_empty.get_field('address') is None

def test_get_description(get_document1, get_empty):
    assert get_document1.get_field('description') == 'Prednisone 20 mg\n        Lialda 2.4 gram'
    assert get_empty.get_field('description') is None

def test_get_direction(get_document1, get_empty):
    assert get_document1.get_field('direction') == 'Prednisone, Taper 5 mg every 3 days,\n    \n    Finish in 2.5 weeks\n    Lialda - take 2 pill everyday for 1 month'
    assert get_empty.get_field('direction') is None

def test_get_refill(get_document1, get_empty):
    assert get_document1.get_field('refill') == '2 times'
    assert get_empty.get_field('refill') is None

def test_parser(get_document1, get_empty):
    get_object = get_document1.parse()
    assert get_object['name'] == 'Maria Sharapova'
    assert get_object['address'] == '9 tennis court, new Russia, DC'
    assert get_object['description'] == 'Prednisone 20 mg\n        Lialda 2.4 gram'
    assert get_object['direction'] == 'Prednisone, Taper 5 mg every 3 days,\n    \n    Finish in 2.5 weeks\n    Lialda - take 2 pill everyday for 1 month'
    assert get_object['refill'] == '2 times'

