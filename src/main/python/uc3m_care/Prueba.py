
import re
import uuid
from pathlib import Path
import json
import datetime
from datetime import date


from uc3m_care.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.vaccine_management_exception import VaccineManagementException
from uc3m_care.vaccination_appoinment import VaccinationAppoinment


def prueba1 ():
    json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
    store_patient = json_files_path + "store_patient.json"

    try:
        with open(store_patient, "r", encoding="utf-8", newline="") as file_p:
            data_list = json.load(file_p)
            patient_id = str()
            patient_system_id2 = str()
            for item in data_list:

                for patient_Id in item["_VaccinePatientRegister__patient_id"]:
                    patient_id = patient_id + patient_Id
                for patientSysId2 in item["_VaccinePatientRegister__patient_sys_id"]:
                    patient_system_id2 = patient_system_id2 + patientSysId2

    except FileNotFoundError:
        date_list = []
    except json.JSONDecodeError as ex:
        raise VaccineManagementException("Json Decode Error - Wrong JSON Format")

    return patient_id

def vaccine_patient(date_signature):

        json_file_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_date = json_file_path + "store_date.json"

        try:
            with open(file_store_date, "r", encoding="utf-8", newline="") as file_d:
                data_list = json.load(file_d)

                date_signature_store = str()
                for item in data_list:

                    for signature in item["_VaccinationAppoinment__date_signature"]:
                        date_signature_store = date_signature_store + signature
                    date_time = item["_VaccinationAppoinment__appoinment_date"]

        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as ex:
            raise VaccineManagementException("JSON decode Error - Wrong JSON Format") from ex

        if date_signature != date_signature_store:
            raise VaccineManagementException('date_signature is not valid')
            ''''
            #DESDE AQUI LA PROFE

                found = true
                date_time = item['_VaccinationAppointment__appointment_date']

            if not found:
                raise VaccineManagementException('date_signature is not valid')
            '''
        today = datetime.today().date()
        date_patient = datetime.fromtimestamp(date_time).date()
        if date_patient != today:
            raise VaccineManagementException('Hoy no es el día')

        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"

        try:
            with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from ex

                # insertamos la fecha
        data_list.append(date_signature.__str__())
        data_list.append(datetime.utcnow().__str__())
        try:
            with open(file_store_vaccine, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
             raise VaccineManagementException("Wrong file or file path") from ex
        return True

print(prueba1())
print(vaccine_patient("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1"))

