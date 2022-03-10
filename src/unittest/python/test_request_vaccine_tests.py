import unittest
from uc3m_care.vaccine_manager import VaccineManager
from uc3m_care.vaccine_management_exception import VaccineManagementException
import os
from pathlib import Path
import json
# import Freezegun revisar estoooo

class MyTestCase(unittest.TestCase):
    def test_request_vaccination_ok( self ):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual(value, "cc49d30252c755d53e4de9794a5918c1")

        # chequeo si esta en el fichero

        with open(file_store,"r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    def test_request_vaccination_ok2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "33")
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Family", "+34123456789", "33")
        self.assertEqual(value, "26b442d86b51e4a583fc8c12af61a446")

        #"chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    def test_request_vaccination_ok3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Family", "+34123456789", "33")
        self.assertEqual(value, "26b442d86b51e4a583fc8c12af61a446")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    def test_request_vaccination_nook(self):
        #patient id hex, not valid
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("zb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("Id received is not a UUID", cm.exception.message)

    def test_request_vaccination_nook2(self):
        #patient id no v4 uuid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("UUID invalid", cm.exception.message)

if __name__ == '__main__':
    unittest.main()
