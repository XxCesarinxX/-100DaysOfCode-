import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time 

class usando_unittest(unittest.TestCase):
    

    def setUp(self):
            self.driver = webdriver.Firefox(executable_path=r"C:\Users\cesar\Documents\geckodriver.exe")
    
    def test_cambiar_ventana(self):
        driver.execute_script("window.open('');")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])

    def test_buscar(self):
        driver= self.driver
        driver.get("https://www.google.com.mx/")
        #self.assertIn("Google", driver.title) #verifica si estamos en Google atravez del titulo
        elemento = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        time.sleep(1)
        #assert  "No se encontro el elemento:" not in driver.page_source

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()