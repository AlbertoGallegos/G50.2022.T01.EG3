import os
from pathlib import Path
import json

import unittest
from freezegun import freeze_time

from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException


class MyTestCase(unittest.TestCase):
    @freeze_time("2022-03-17")
    def test_request_vaccination_ok(self):
        # Comprobacion uuid e insercion del paciente correcta
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
        "Pedro Perez Jimenez de la Rue", "Regular", "+34123456789", "6")
        self.assertEqual(value, "53c1e4289490e94b54c737dc402dfc54")

        # chequeo si esta en el fichero

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok2(self):
        # Comprobacion insercion del paciente y de un familiar correcta
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "33")
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Family", "+34123456789", "33")
        self.assertEqual(value, "1a35a9ba1bc30f0f56737202cea418cf")

        # chequeo si esta en el fichero

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok3(self):
        # Comprobacion insercion de un familiar correcta
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
        "Pedro Perez Jimenez de la Sien", "Family", "+34123456789", "7")
        self.assertEqual(value, "4b46ffe83a98e712e70e0486b9a2ab0f")

        # chequeo si esta en el fichero

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok4(self):
        # Comprobacion valores limite edad correcta 124
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "124")
        self.assertEqual(value, "5f5d1f64ae3a736ff515697f615e15e4")

        # chequeo si esta en el fichero

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok5(self):
        # Comprobacion valores limite edad correcta 125
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_request = VaccineManager()
        value = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                  "Pedro Perez", "Regular", "+34123456789", "125")
        self.assertEqual(value, "71a02a010a5ec57b498890003a55f647")

        # chequeo si esta en el fichero

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_VaccinePatientRegister__patient_id"] == \
                    "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
                found = True
        self.assertTrue(found)

    @freeze_time("2022-03-17")
    def test_request_vaccination_ok6(self):
        # Comprobacion diferentes pacientes diferente MD5
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store = json_files_path + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        my_request = VaccineManager()
        value1 = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
        "Pedro Perez", "Family", "+34123456789", "13")
        value2 = my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
        "Alfonso Perez", "Family", "+34123456789", "10")

        self.assertNotEqual(value1, value2)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook(self):
        # patient id no v4 uuid
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-113f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("UUID invalid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook2(self):
        # patient id hex, not valid
        my_request = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("zb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("Id received is not a UUID", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook3(self):
        # Comprobacion registration type no valido
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Individual", "+34123456789", "33")
        self.assertEqual("Registration type is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook4(self):
        # Comprobacion valor limite nombre con 31 caracteres
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
            "Pedro Perez Jimenez de la Cuina", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook5(self):
        # Comprobacion nombre sin dos cadenas separadas por un blanco
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "PedroPerez", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook6(self):
        # Comprobacion no hay un nombre introducido
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook7(self):
        # Comprobacion nombre sin dos cadenas separadas por un blanco
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedr5 Ferna*dez", "Regular", "+34123456789", "33")
        self.assertEqual("name surname is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook8(self):
        # Comprobacion valor limite numero de telefono no valido un numero menos
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+3423456789", "33")
        self.assertEqual("phone number is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook9(self):
        # Comprobacion valor limite numero de telefono no valido un numero mas
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+341234567890", "33")
        self.assertEqual("phone number is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook10(self):
        # Comprobacion no se trata de un numero de telefono
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "telefono", "33")
        self.assertEqual("phone number is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook11(self):
        # Comprobacion no se trata de un numero de telefono
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "123456789", "33")
        self.assertEqual("phone number is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook12(self):
        # Comprobacion valores limites edad no valido 5
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "5")
        self.assertEqual("age is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook13(self):
        # Comprobacion valores limites edad no valido 126
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "126")
        self.assertEqual("age is not valid", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook14(self):
        # Comprobacion id del paciente ya registrada
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "7,5")
        self.assertEqual("age is not numeric", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook15(self):
        # age not numeric
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "cinco")
        self.assertEqual("age is not numeric", c_m.exception.message)

    @freeze_time("2022-03-17")
    def test_request_vaccination_nook16(self):
        # Comprobacion id del paciente ya registrada
        my_request = VaccineManager()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                              "Pedro Perez", "Regular", "+34123456789", "33")
            my_request.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                             "Pedro Perez", "Regular", "+34123456789", "33")
        self.assertEqual("patient_id registered", c_m.exception.message)

if __name__ == '__main__':
    unittest.main()
