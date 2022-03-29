"""Module """
import re
import uuid
from pathlib import Path
import json

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

    @staticmethod
    def validate_alg(alg):
        if alg != "SHA-256":
             VaccineManagementException("alg is not valid")

    @staticmethod
    def validate_typ(typ):
        if typ != "DS":
            VaccineManagementException("typ is not valid")

    @staticmethod
    def validate_issue_at(issue_at):
        pass


    def get_vaccine_date(self, input_file):
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)

                patient_system_id = ""
                contact_phone_number = ""

                for patientSysId in data_list["PatientSystemID"]:
                    patient_system_id = patient_system_id + patientSysId
                for contactPhone in data_list["ContactPhoneNumber"]:
                    contact_phone_number = contact_phone_number + contactPhone

        except FileNotFoundError:
            date_list = []
        except json.JSONDecodeError as ex:
            raise VaccineManagementException("Json Decode Error - wrong JSON Format")

        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_date = json_files_path + "store_date.json"
        self.validate_alg(alg)
        self.validate_typ(typ)
        self.validate_patient_system_id(patient_system_id, patient_id)
        self.validate_issued_at(issued_at)
        self.validate_vaccinationdate(vaccinationdate)
        self.validate_datesignature(datesignature)

        request_vaccination_id()
        if self.validate_guid(patient_system_id):
            my_appointment = \
                VaccinationAppoinment(patient_id, patient_sys_id, patient_phone_number, days)

            try:
                with open(file_store_date, "r", encoding="utf-8", newline="") as file:
                    data_list = json.load(file)
            except FileNotFoundError:
                # file is not found , so  init my data_list
                data_list = []
            except json.JSONDecodeError as ex:
                raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from ex

            found = False
            for item in data_list:
                if item["PatientSystemId"] == patient_system_id and \
                        (item["ContactPhoneNumber"] == contact_phone_number):
                    found = True

            if found is False:
                data_list.append(my_appointment.__dict__)

            try:
                with open(file_store_date, "w", encoding="utf-8", newline="") as file:
                    json.dump(data_list, file, indent=2)
            except FileNotFoundError as ex:
                raise VaccineManagementException("Wrong file or file path") from ex

            if found is True:
                raise VaccineManagementException("date registered")

        return my_appointment.vaccination_signature

    # HAY QUE CAMBIAR LA FUNCION
    ''' def vaccine_patient():
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        self.validate_name(name)
        self.validate_registration_type(registration_type)
        self.validate_phone_number(phone_number)
        self.validate_age(age)
        if self.validate_guid(patient_id):
            my_register = \
            VaccinePatientRegister(patient_id, name, registration_type, phone_number, age)

            #DESDE AQUI LA PROFE

                found = true
                date_time = item['_VaccinationAppointment__appointment_date']

            if not found:
                raise VaccineManagementException('date_signature is not valid')

            today = datetime.today().date()
            date_patient= datetime.fromtimestamp(date_time).date()
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
            return True'''
