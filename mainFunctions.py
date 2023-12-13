from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


#FUNÇÃO PARA VERIFICAR SE O ELEMENTO ESTÁ VISIVEL
def checkElement(par_driver, par_xpath):
    try:
        element = WebDriverWait(par_driver, 5).until(EC.presence_of_element_located((By.XPATH, par_xpath)))
        if element: 
            print('ELEMENTO ESTÁ VISIVEL')
            return element
    except:
        print('ELEMENTO NÃO ESTÁ VISIVEL')
        return False

#FUNÇÃO PARA FECHAR O POPUP
def clearPopUp(par_driver, par_popup):
    try:
        par_popup = WebDriverWait(par_driver, 5).until(EC.presence_of_element_located((By.XPATH, par_popup)))
        par_popup.click()
    except:
            pass
    
#FUNÇÃO PARA DIGITAR O TEXTO
def typeText(par_driver, par_xpath, par_text):
    element = WebDriverWait(par_driver, 5).until(EC.presence_of_element_located((By.XPATH, par_xpath)))
    element.send_keys(par_text)

#UNÇÃO PARA CLICAR NO BOTÃO
def clickButton(par_driver, par_xpath, check_button):
    if check_button:
        element = WebDriverWait(par_driver, 5).until(EC.presence_of_element_located((By.XPATH, par_xpath)))
        element.click()
        print('BOTAO CLICADO')
    else:
         print('BOTAO NÃO EXISTE')
         par_driver.quit()


#FUNÇÃO PARA VARIAR O TEMPO DE DIGITAÇÃO 
def waitType(par_driver, par_xpath, par_text, time_min, time_max):
     caracteres = list(par_text)
     for i in caracteres:
        tempo = random.randint(time_min, time_max)
        tempo /= 1000
        typeText(par_driver, par_xpath, i)
        sleep(tempo)