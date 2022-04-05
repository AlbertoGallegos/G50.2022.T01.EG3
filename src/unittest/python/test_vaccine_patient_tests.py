import os
from pathlib import Path
import json
import hashlib

import unittest
from freezegun import freeze_time

from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException

class MyTestCase(unittest.TestCase):
    @freeze_time('2022-03-17')
    def setup(self):
        # funcion con datos preparados 10 días antes de la fecha de la cita

        # preparacion de la estructura de alamcenes
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_patient = json_files_path + "store_patient.json"
        file_store_date = json_files_path + "store_date.json"
        file_test = json_files_path + "Rf2/test_ok.json"

        my_manager = VaccineManager()
        if os.path.isfile(file_store_patient):
            os.remove(file_store_patient)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)


        # añado al paciente al almacen
        my_manager.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
            "Pedro Perez Jimenez de la Rue", "Regular", "+34123456789", "6")
        # añado la cita al almacen
        my_manager.get_vaccine_date(file_test)

    @freeze_time('2022-03-17')
    def setup_2(self):
        # funcion con datos preparados 10 días antes de la fecha de la cita

        # preparacion de la estructura de alamcenes
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_patient = json_files_path + "store_patient.json"
        file_store_date = json_files_path + "store_date.json"
        file_test = json_files_path + "Rf2/test_ok.json"
        file_test_2 = json_files_path + "Rf2/test_ok_2.json"

        my_manager = VaccineManager()
        if os.path.isfile(file_store_patient):
            os.remove(file_store_patient)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)

        # añado al paciente al almacen
        my_manager.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
            "Pedro Perez Jimenez de la Rue", "Regular", "+34123456789", "6")
        my_manager.get_vaccine_date(file_test)

        # añado al segundo paciente al amacen
        my_manager.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
            "Rocio Perez Jimenez de la Rue", "Family", "+34123456789", "15")
        my_manager.get_vaccine_date(file_test_2)

    @freeze_time('2022-03-27')
    def test_vaccine_patient_ok(self):
        # comprobamos el camino 1, correcto pasa 1 vez por el bucle for
        self.setup()
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        if os.path.isfile(file_store_vaccine):
            os.remove(file_store_vaccine)
        my_manager = VaccineManager()

        value = my_manager.vaccine_patient\
            ("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1")
        self.assertEqual(value, True)

        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        if data_list[0] == \
            "2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1" and \
            data_list[1] == "2022-03-27 00:00:00":
            found = True

        self.assertTrue(found)

    @freeze_time('2022-03-27')
    def test_vaccine_patient_ok2(self):
        # comprobamos el camino 1, correcto pasa 2 veces por el bucle for
        self.setup_2()
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        if os.path.isfile(file_store_vaccine):
            os.remove(file_store_vaccine)
        my_manager = VaccineManager()

        value = my_manager.vaccine_patient\
            ("15c9755ccb8307d808e0ace5821e6b0940130b7b3b493eebfbf2d1aaf39976fb")
        self.assertEqual(value, True)

        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)

        found = False
        if data_list[0] == \
            "15c9755ccb8307d808e0ace5821e6b0940130b7b3b493eebfbf2d1aaf39976fb" and \
            data_list[1] == "2022-03-27 00:00:00":
            found = True

        self.assertTrue(found)

    @freeze_time('2022-03-27')
    def test_vaccine_patient_nook(self):
        # comprobamos el camino 2 no ejecuto get_vaccine_date \
        # y no se crea store_date, no entra en el bucle for
        # prepararo la estructura de almacenes
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        file_store_patient = json_files_path + "store_patient.json"
        file_store_date = json_files_path + "store_date.json"

        my_manager = VaccineManager()
        if os.path.isfile(file_store_patient):
            os.remove(file_store_patient)
        if os.path.isfile(file_store_date):
            os.remove(file_store_date)

        # añado al paciente al almacen
        my_manager.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
            "Pedro Perez Jimenez de la Rue", "Regular", "+34123456789", "6")

        # leo el fichero para comparar el contenido antes y después de la llamada del método
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.vaccine_patient\
                ("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1")
        self.assertEqual(c_m.exception.message, "Store_date does not exist")

        # leemos otra vez el archivo para comparar
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            hash_new = hashlib.md5(file.__str__().encode()).hexdigest()

        if hash_original == hash_new:
            file_is_equal = True
            self.assertTrue(file_is_equal)

    @freeze_time('2022-03-27')
    def test_vaccine_patient_nook2(self):
        # Comprobamos el camino 3, excepción date signature not valid
        self.setup()
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        my_manager = VaccineManager()

        # leo el fichero para comparar el contenido antes y después de la llamada del método
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.vaccine_patient\
                ("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac18")
        self.assertEqual(c_m.exception.message, "Date signature is not valid")

        # leemos otra vez el archivo para comparar
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            hash_new = hashlib.md5(file.__str__().encode()).hexdigest()

        if hash_original == hash_new:
            file_is_equal = True
            self.assertTrue(file_is_equal)

    @freeze_time('2022-03-27')
    def test_vaccine_patient_nook3(self):
        # Comprobamos el camino 4, excepción date signature not found
        self.setup()
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        my_manager = VaccineManager()

        # leo el fichero para comparar el contenido antes y después de la llamada del método
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()

        # cadena no encontrada
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.vaccine_patient\
                ("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac8")
        self.assertEqual(c_m.exception.message, "Date signature not found")

        # leemos otra vez el archivo para comparar
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            hash_new = hashlib.md5(file.__str__().encode()).hexdigest()

        if hash_original == hash_new:
            file_is_equal = True
            self.assertTrue(file_is_equal)

    @freeze_time('2022-03-26')
    def test_vaccine_patient_nook4(self):
        # Comprobamos el camino 5, excepción today is not the day 1 día antes
        self.setup()
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        my_manager = VaccineManager()

        # leo el fichero para comparar el contenido antes y después de la llamada del método
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.vaccine_patient\
                ("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1")
        self.assertEqual(c_m.exception.message, "Today is not the day")

        # leemos otra vez el archivo para comparar
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            hash_new = hashlib.md5(file.__str__().encode()).hexdigest()

        if hash_original == hash_new:
            file_is_equal = True
            self.assertTrue(file_is_equal)

    @freeze_time('2022-03-28')
    def test_vaccine_patient_nook5(self):
        # Comprobamos el camino 5, excepción today is not the day 1 día después
        self.setup()
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_vaccine = json_files_path + "store_vaccine.json"
        my_manager = VaccineManager()

        # leo el fichero para comparar el contenido antes y después de la llamada del método
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file_org:
            hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()

        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.vaccine_patient\
                ("2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1")
        self.assertEqual(c_m.exception.message, "Today is not the day")

        # leemos otra vez el archivo para comparar
        with open(file_store_vaccine, "r", encoding="utf-8", newline="") as file:
            hash_new = hashlib.md5(file.__str__().encode()).hexdigest()

        if hash_original == hash_new:
            file_is_equal = True
            self.assertTrue(file_is_equal)