import utilise
from Prescription_Parser import PrescriptionParser
from Patient_parser import PatientParser

path_prescription1 = '../resources/prescription/pre_1.pdf'
path_prescription2 = '../resources/prescription/pre_2.pdf'
path_patient2 = '../resources/patient_details/pd_2.pdf'
def extractor(file_path, file_type):
    #Extract data from pdf file
    convert_text =utilise.get_text_from_pdf(file_path)
    # return convert_text
# #Extract file pdf from path to direct class to get result#
    if file_type == 'prescription':
        pp = PrescriptionParser(convert_text).parser()
        return pp
    elif file_type == 'patient':
        pp = PatientParser(convert_text).parser()
        return pp


if __name__ == '__main__':
    data = extractor(path_prescription2, 'prescription')
    print(data)

