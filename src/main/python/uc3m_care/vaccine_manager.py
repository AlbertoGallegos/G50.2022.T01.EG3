"""Module """
import re
import uuid
from pathlib import Path
import json

from uc3m_care.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.vaccine_management_exception import VaccineManagementException

class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""
    def __init__(self):
        pass

    @staticmethod
    def validate_guid(guid):
        try:
            uuid.UUID(guid)
            myregex = \
            re.compile(r'^[0-9A-Fa-z]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$',\
            re.IGNORECASE)
            res = myregex.fullmatch(guid)

            if not res:
                raise VaccineManagementException("UUID invalid")
        except ValueError as err:
            raise VaccineManagementException("Id received is not a UUID") from err
        return True

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
            if (int(age) < 6 or int(age) > 125 ):
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
