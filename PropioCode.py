import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import click


def busqueda():
    driver.get("https://www.google.com.mx/")
    search = driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
    search.send_keys(busquedas, Keys.ARROW_DOWN)
    time.sleep(1)
    search.send_keys(Keys.ENTER)
    time.sleep(3)
    resultados = driver.find_elements_by_tag_name("h3")
    ca = 0
    for numero in resultados:
        ca= ca + 1
    print("paguinas obtenidas", ca)
    paguina = int(input("que paguina desea utilizar\n\t-->"))
    resultados[paguina].click()
    time.sleep(1)

def cambio_ventna():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])

def resoomer():
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://resoomer.com/es/")
    importar = driver.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[1]/div/form/fieldset/div/textarea")
    importar.send_keys(url)
    time.sleep(2)
    button = driver.find_element_by_xpath("/html/body/section[1]/div/div[2]/div[1]/div/form/fieldset/div/div[1]/div/ul/li[2]/input")
    button.click()


informacion="https://es.wikipedia.org/wiki/Historia_de_M%C3%A9xico"
print("Que es lo que desa resumir el dia de hoy, galan")
busquedas = input()
driver = webdriver.Firefox(executable_path=r"C:\Users\cesar\Documents\geckodriver.exe")
busqueda()
url = driver.current_url
resoomer()