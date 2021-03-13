#TomasPerez
#https://github.com/TomasVPerez

from selenium import webdriver
import pyautogui, time, subprocess

urlFisica = "https://ortuy.zoom.us/j/95005927377?pwd=Y0F6dVZTL3MyMmhrcGJDQzk4TThCZz09#success"
urlProg = "https://ortuy.zoom.us/j/98456775707?pwd=Tk5WZEhwS3YvUlBGMmo3OGx1UHNXUT09#success"
urlFund = "https://ortuy.zoom.us/j/99791591627?pwd=UHcwUkNGaDFvcUJ3Q0tmdVRjaWtKZz09#success"

opciones = webdriver.ChromeOptions()
opciones.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome = webdriver.Chrome(options=opciones)

def iniciarClase(url):
    chrome.get(url)
    inicio = chrome.find_element_by_xpath('//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div')
    inicio.click()
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

fechaActual = time.ctime()
dia = fechaActual.split(" ")[0]
horaExacta = fechaActual.split(" ")[3]
hora = horaExacta.split(":")[0]

while True:
    if dia == "Mon" and hora == "08" or dia == "Tue" and hora == "10" or dia == "Fri" and hora == "08":
        iniciarClase(urlProg)
        time.sleep(10)
        chrome.close()
        break
    if dia == "Mon" and hora == "10" or dia == "Thu" and hora == "10":
        iniciarClase(urlFund)
        time.sleep(10)
        chrome.close()
        break
    if dia == "Tue" and hora == "08" or dia == "Wed" and hora == "10": 
        iniciarClase(urlFisica)
        time.sleep(10)
        chrome.close()
        #subprocess.call("taskkill /f /im py.exe", shell=True)
        break
    else:
        chrome.close()
        print("No tenes clase!")
        break




