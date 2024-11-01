from Backend.src.Patient_Parser import  PatientPaser
import pytest


@pytest.fixture
def get_document():
    document = '''
    page : 1
    Patient Information
    Birthday
    Kathy Crawford June 6 1972
    (737) 988-0851
    9264 Ash Dr
    New York City, 10005
    United States
    
    in Case of Emergency
    
    Simeone Crawford
    
    Home phone
    (990) 375-4621
    Genera! Medical History
    
    Chicken Pox (Varicella):
    IMMUNE
    Have you had the Hepatitis B vaccination?
    
    No
    
    4711242020
    
    Birth Date
    May 6 1972
    
    Weight’
    95
    Height:
    190
    
    eo
    
    eel
    
    9266 Ash Dr
    New York City, New York, 10005
    United States
    
    Work phone
    
    Measles:
    
    IMMUNE
    
    List any Medical Problems (asthma, seizures, headaches):
    
    Migraine
    
    '''
    return PatientPaser(document)

@pytest.fixture
def get_empty():
    return PatientPaser('')

def test_get_name(get_document, get_empty):
    assert get_document.get_name() == 'Kathy Crawford'
    # assert get_empty.get_field('name') is None

def test_address(get_document, get_empty):
    assert get_document.get_field('address') == '9264 Ash Dr\n    New York City, 10005\n    United States'

def test_phone(get_document, get_empty):
    assert get_document.get_field('phone') == '(737) 988-0851'

def test_vaccination(get_document, get_empty):
    assert get_document.get_field('vaccination') == 'No'

def test_medical_problems(get_document, get_empty):
    assert get_document.get_field('medical_problem') == 'Migraine'