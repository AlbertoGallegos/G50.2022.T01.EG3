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
       # preparacion de la estructura de alamcenes
       json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
       json_files_path2 = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/Rf2"
       file_store_patient = json_files_path + "store_patient.json"
       file_store_date = json_files_path + "store_date.json"
       file_test = json_files_path2 + "test_ok.json"

       my_manager = VaccineManager()
       if os.path.isfile(file_store_patient):
           os.remove(file_store_patient)
       if os.path.isfile(file_store_date):
           os.remove(file_store_date)

       # añado al paciente al almacen
       my_manager.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                                 "Pedro Perez Jimenez de la Rue", "Regular", "+34123456789", "6")
       # Compruebo el metodo
       value = my_manager.get_vaccine_date(file_test)
       self.assertEqual(value, "2f61ce90ae7d11c3bd9cfae77a17097c0716fd1eb39df725641d46b62e85bac1")

       # compruebo la fecha de la cita
       with open(file_store_date, "r", encoding="utf-8", newline="") as file:
           data_list = json.load(file)
       found = False
       for item in data_list:
            if item["_VaccinationAppoinment__patient_id"] == "bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0":
               found = True
       self.assertTrue(found)

   @freeze_time('2022-03-17')
   def test_get_vaccine_date_nodosnook(self):
        
        json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
        file_store_date = json_files_path + "store_date.json"
        my_manager = VaccineManager()

        json_files_rf2_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/Rf2/"
        for p1,p2 in param_list_nook:
            with self.subTest(test=p1):
                file_test = json_files_rf2_path + p1

                # leo el fichero para comparar el contenido antes y después de la llamada del método
        
                with open(file_store_date, "r", encoding="utf-8", newline="") as file_org:
                    hash_original = hashlib.md5(file_org.__str__().encode()).hexdigest()
                    
                # chequeo el metodo
                with self.assertRaises(VaccineManagementException) as cm:
                    value = my_manager.get_vaccine_date(file_test)
                self.assertEqual(cm.exception.message, p2)
        
                #leemos otra vez el archivo para comparar
                with open(file_store_date, "r", encoding="utf-8", newline="") as file:
                    hash_new = hashlib.md5(file.__str__().encode()).hexdigest()
                if hash_original == hash_new:
                    file_is_equal = True
                self.assertTrue(file_is_equal)

   @freeze_time('2022-03-17')
   def test_get_vaccine_date_nook(self):
       json_files_rf2_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/Rf2/"
       file_test = json_files_rf2_path + "test_ok.json"
       my_manager = VaccineManager()
       json_files_path = str(Path.home()) + "/PycharmProjects/G50.2022.T01.EG3/src/JsonFiles/"
       file_store = json_files_path + "store_patient.json"
       if os.path.isfile(file_store):
           os.remove(file_store)

       # añado al paciente al almacen
       my_manager.request_vaccination_id("bb5dbd6f-d8b4-413f-8eb9-dd262cfc54e0",
                                             "Pedro Ramon Puig", "Regular", "+34123456789", "23")

       # chequeo el metodo
       with self.assertRaises(VaccineManagementException) as cm:
            my_manager.get_vaccine_date(file_test)
       self.assertEqual(cm.exception.message, "patient_system_id is different")
