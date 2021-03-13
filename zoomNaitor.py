#TomasPerez
#https://github.com/TomasVPerez

from selenium import webdriver
import pyautogui, time, subprocess

urlFisica = #urls de las clases de zoom. 

opciones = webdriver.ChromeOptions()
opciones.add_experimental_option('excludeSwitches', ['enable-logging']) #Saca alertas molestas de la consola.
chrome = webdriver.Chrome(options=opciones)

def iniciarClase(url):
    chrome.get(url)
    inicio = chrome.find_element_by_xpath('//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div')
    inicio.click()
    time.sleep(2)
    pyautogui.press("tab") #Se apreta el tabulador dos veces y el enter para aceptar el popup.
    pyautogui.press("tab")
    pyautogui.press("enter")

fechaActual = time.ctime()
dia = fechaActual.split(" ")[0]
horaExacta = fechaActual.split(" ")[3]
hora = horaExacta.split(":")[0]

while True:
    if dia == "Mon" and hora == "15" or dia == "Tue" and hora == "10" or dia == "Fri" and hora == "08": #Copiar y pegar para agregar materias. Cambiar los dias y horarios.
        iniciarClase(urlFisica)
        time.sleep(10) #Espera 10 segundos y cierra la pestaña
        chrome.close()
        break
    else:
        chrome.close()
        print("No tenes clase!")
        break




