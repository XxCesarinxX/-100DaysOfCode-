import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time 


def busqueda():
    driver.get("https://www.google.com.mx/")
    search = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    search.send_keys(busquedas, Keys.ARROW_DOWN)
    time.sleep(1)
    search.send_keys(Keys.ENTER)

def cambio_ventna():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

def resoomer():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://resoomer.com/es/")
    importar = driver.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[1]/div/form/fieldset/div/textarea")
    importar.send_keys(informacion)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[1]/div/form/fieldset/div/div[1]/div/ul/li[2]/input").click
    


informacion="palabra reservada para el Url que se desea obtener"
print("Que es lo que desa resumir el dia de hoy, galan")
busquedas = input()
driver = webdriver.Firefox(executable_path=r"C:\Users\cesar\Documents\geckodriver.exe")
busqueda()
cambio_ventna()
resoomer()
