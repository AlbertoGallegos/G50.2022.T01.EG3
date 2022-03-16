import os
from pathlib import Path

import unittest
from freezegun import freeze_time

from uc3m_care.vaccine_manager import VaccineManager
from uc3m_care.vaccine_management_exception import VaccineManagementException
import json
# import Freezegun revisar estoooo

class MyTestCase(unittest.TestCase):
    @freeze_time("2022-03-17")
    def test_request_vaccination_ok( self ):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual(value, "69e2c6adb20c01016918438fce92974d")

        # chequeo si esta en el fichero

        with open(file_store,"r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
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
        self.assertEqual(value, "eeec268711e148069ef6c06f261dbc78")

        #"chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Family", "+34123456789", "33")
        self.assertEqual(value, "eeec268711e148069ef6c06f261dbc78")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook(self):
        #patient id hex, not valid
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("zb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("Id received is not a UUID", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook2(self):
        #patient id no v4 uuid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("UUID invalid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook2(self):
        #patient id no v4 uuid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("UUID invalid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook3(self):
        #age not numeric
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "cinco")
        self.assertEqual("age is not numeric", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook4(self):
        #age not valid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "5")
        self.assertEqual("age is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook4(self):
        # age not valid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "126")
        self.assertEqual("age is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook5(self):
        # phone number not valid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+3423456789", "33")
        self.assertEqual("phone number is not valid", cm.exception.message)

if __name__ == '__main__':
    unittest.main()
