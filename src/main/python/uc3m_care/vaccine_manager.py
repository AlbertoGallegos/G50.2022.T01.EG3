"""Module """
import re
import uuid
from pathlib import Path
import json
from datetime import datetime

from uc3m_care.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.vaccine_management_exception import VaccineManagementException
from uc3m_care.vaccination_appoinment import VaccinationAppoinment


class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""

    def __init__(self):
        pass

    @staticmethod
    def validate_guid(guid):
        try:
            uuid.UUID(guid)
            myregex = \
                re.compile(r'^[0-9A-Fa-z]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$', \
                           re.IGNORECASE)
            res = myregex.fullmatch(guid)

            if not res:
                raise VaccineManagementException("UUID invalid")
        except ValueError as err:
            raise VaccineManagementException("Id received is not a UUID") from err
        return True

    @staticmethod
    def validate_patient_sys_id(patientsysid):
        myregex = re.compile(r'^[a-f0-9]{32}$', re.IGNORECASE)
        res = myregex.fullmatch(patientsysid)

        if not res:
            raise VaccineManagementException("Patient Sys ID is not valid")

    @staticmethod
    def validate_date_signature(datesignature):
        myregex = re.compile(r'^[a-f0-9]{64}$', re.IGNORECASE)
        res = myregex.fullmatch(datesignature)

        if not res:
            raise VaccineManagementException("Date signature is not valid")
        
    @staticmethod
    def validate_registration_type(registration_type):
        myregex = re.compile(r'(Regular|Family)')
        res = myregex.fullmatch(registration_type)
        if not res:
            raise VaccineManagementException("Registration type is not valid")

    @staticmethod
    def validate_name(name):
        myregex = re.compile(r'^(?=.{1,30}$)(([a-zA-Z)]+\s)+[a-zA-Z]+)$')
        res = myregex.fullmatch(name)
        if not res:
            raise VaccineManagementException("name surname is not valid")

    @staticmethod
    def validate_phone_number(phone_number):
        myregex = re.compile(r'^(\+)[0-9]{11}')
        res = myregex.fullmatch(phone_number)
        if not res:
            raise VaccineManagementException("phone number is not valid")

    @staticmethod
    def validate_age(age):
        if age.isnumeric():
            if (int(age) < 6 or int(age) > 125):
                raise VaccineManagementException("age is not valid")
        else:
            raise VaccineManagementException("age is not numeric")

    def request_vaccination_id(self, patient_id, name, registration_type, phone_number, age):
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        self.validate_name(name)
        self.validate_registration_type(registration_type)
        self.validate_phone_number(phone_number)
        self.validate_age(age)
        if self.validate_guid(patient_id):
            my_register = \
                VaccinePatientRegister(patient_id, name, registration_type, phone_number, age)

            try:
                with open(file_store, "r", encoding="utf-8", newline="") as file:
                    data_list = json.load(file)
            except FileNotFoundError:
                # file is not found , so  init my data_list
                data_list = []
            except json.JSONDecodeError as ex:
                raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from ex

            found = False
            for item in data_list:
                if item["_VaccinePatientRegister__patient_id"] == patient_id and \
                        (item["_VaccinePatientRegister__registration_type"] == registration_type) and \
                        (item["_VaccinePatientRegister__full_name"] == name) and \
                        (item["_VaccinePatientRegister__phone_number"] == phone_number) and \
                        (item["_VaccinePatientRegister__age"] == age):
                    found = True

            if found is False:
                data_list.append(my_register.__dict__)

            try:
                with open(file_store, "w", encoding="utf-8", newline="") as file:
                    json.dump(data_list, file, indent=2)
            except FileNotFoundError as ex:
                raise VaccineManagementException("Wrong file or file path") from ex

            if found is True:
                raise VaccineManagementException("patient_id registered")

            return my_register.patient_system_id


    def get_vaccine_date(self, input_file):

        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)

                patient_system_id = str()
                contact_phone_number = str()

                try:
                    for patientSysId in data_list["PatientSystemID"]:
                        patient_system_id = patient_system_id + patientSysId
                    for contactPhone in data_list["ContactPhoneNumber"]:
                        contact_phone_number = contact_phone_number + contactPhone
                except KeyError as ex:
                    raise VaccineManagementException("Key not found or key Error") from ex

        except json.JSONDecodeError as ex:
            raise VaccineManagementException("JSON Decode Error - Wrong input JSON Format") from ex

        self.validate_patient_sys_id(patient_system_id)
        self.validate_phone_number(contact_phone_number)

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

        except json.JSONDecodeError as ex:
            raise VaccineManagementException("Json Decode Error - Wrong store_patient JSON Format") from ex

        if patient_system_id == patient_system_id2:
            my_appointment = \
                VaccinationAppoinment(patient_id,patient_system_id,contact_phone_number,10)
        else:
            raise VaccineManagementException("patient_system_id is different")

        file_store_date = json_files_path + "store_date.json"

        try:
            with open(file_store_date, "r", encoding="utf-8", newline="") as file_d:
                data_list = json.load(file_d)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from ex

        found = False
        if found is False:
            data_list.append(my_appointment.__dict__)

        try:
            with open(file_store_date, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        return my_appointment.vaccination_signature

    def vaccine_patient(self, datesignature):
        json_file_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_date = json_file_path + "store_date.json"

        self.validate_date_signature(datesignature)
        try:
            with open(file_store_date, "r", encoding="utf-8", newline="") as file_d:
                data_list = json.load(file_d)

                found = False
                for item in data_list:
                    if item["_VaccinationAppoinment__date_signature"] == datesignature:
                        found = True
                        vaccination_date = item["_VaccinationAppoinment__appoinment_date"]
                if not found:
                    raise VaccineManagementException("Date signature not found")

        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as ex:
            raise VaccineManagementException("JSON decode Error - Wrong JSON Format") from ex

        today = datetime.today().date()
        date_patient = datetime.fromtimestamp(vaccination_date).date()
        if date_patient != today:
            raise VaccineManagementException('Hoy no es el día')

        file_store_vaccine = json_file_path + "store_vaccine.json"

        try:
            with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file_v:
                data_list = json.load(file_v)
        except FileNotFoundError:
            # file is not found , so  init my data_list
            data_list = []
        except json.JSONDecodeError as ex:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from ex

        # insertamos la fecha
        data_list.append(datesignature.__str__())
        data_list.append(datetime.utcnow().__str__())
        try:
            with open(file_store_vaccine, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
             raise VaccineManagementException("Wrong file or file path") from ex
        return True
