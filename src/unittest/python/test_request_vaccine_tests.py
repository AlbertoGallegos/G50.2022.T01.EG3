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
        # Comprobacion uuid e insercion del paciente correcta
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
        # Comprobacion insercion del paciente y de un familiar correcta
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
        # Comprobacion insercion de un familiar correcta
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
    def test_request_vaccination_ok4(self):
        # Comprobacion valores limite edad correcta 6
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "6")
        self.assertEqual(value, "b963b99d137d7ff80259ba2fda79d515")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok5(self):
        # Comprobacion valores limite edad correcta 7
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "7")
        self.assertEqual(value, "00fdcce18752bc353519d6eac12fdc38")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok6(self):
        # Comprobacion valores limite edad correcta 125
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "125")
        self.assertEqual(value, "4e76ab9aeb1eaf43ee56549c4cb1795d")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok7(self):
        # Comprobacion valores limite edad correcta 124
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "124")
        self.assertEqual(value, "95c6ac84d8d2fc039c7463f0456d5a54")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok8(self):
        # Comprobacion valores limite correcto del nombre con 30 caracteres
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez Jimenez de la Sien", "Regular", "+34123456789", "33")
        self.assertEqual(value, "b23dae25908b4c364db772256f97589e")

        "chequeo si esta en el fichero"

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok8(self):
        # Comprobacion valores limite correcto del nombre con 29 caracteres
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez Jimenez de la Rue", "Regular", "+34123456789", "33")
        self.assertEqual(value, "ee84ee232758cdebf735c2f724b05c86")

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
        # Comprobacion valores limites edad no valido 126
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "126")
        self.assertEqual("age is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook5(self):
        # Comprobacion valores limites edad no valido 5
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "5")
        self.assertEqual("age is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook6(self):
        # Comprobacion valor limite numero de telefono no valido un numero menos
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+3423456789", "33")
        self.assertEqual("phone number is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook7(self):
        # Comprobacion valor limite numero de telefono no valido un numero mas
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+341234567890", "33")
        self.assertEqual("phone number is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook8(self):
        # Comprobacion no se trata de un numero de telefono
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "telefono", "33")
        self.assertEqual("phone number is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook9(self):
        # Comprobacion nombre sin dos cadenas separadas por un blanco
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "PedroPerez", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook10(self):
        # Comprobacion no hay un nombre introducido
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook11(self):
        # Comprobacion valor limite nombre con 31 caracteres
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez Jimenez de la Cuina", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook12(self):
        # Comprobacion registration type no valido
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Individual", "+34123456789", "33")
        self.assertEqual("Registration type is not valid", cm.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook13(self):
        # Comprobacion id del paciente ya registrada
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as cm:
            value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                      "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("patient_id registered", cm.exception.message)


if __name__ == '__main__':
    unittest.main()
