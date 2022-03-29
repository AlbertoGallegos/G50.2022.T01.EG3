
from pathlib import Path
import json



def prueba1 ():
    json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/Rf2/"
    file_date = json_files_path + "test_ok.json"
    fileP = open(file_date, "r", encoding="utf-8", newline="")
    jsondecode = json.load(fileP)

    patient_system_id = ""
    contact_phone_number = ""

    for patientSysId in jsondecode["PatientSystemID"]:
        patient_system_id = patient_system_id + patientSysId
    for contactPhone in jsondecode["ContactPhoneNumber"]:
        contact_phone_number =  contact_phone_number + contactPhone

    return patient_system_id, contact_phone_number



print(prueba1())

