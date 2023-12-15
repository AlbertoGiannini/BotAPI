import requests
import random
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from mainFunctions import clearPopUp, checkElement, typeText, clickButton
from time import sleep

#CONFIGURANDO O WEBDRIVER DO CHROME
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])


driver = webdriver.Chrome(options=chrome_options)

#CREDENCIAIS PARA ACESSAR A API
api_key = "SUA_CHAVE_DA_API" #SUA CHAVE PARA ACESSAR A API
base_url = "https://api.maersk.com/reference-data/vessels" #LINK DA SUA API
headers = {
 "Consumer-Key": api_key
}
#PASSAR AS CREDENCIAIS DA API COMO PARÂMETROS NA REQUEST
response = requests.get(base_url, headers=headers)


#DEFININDO O CAMINHO DO DRIVER
driver.get('https://www.marinetraffic.com/en/ais/home/centerx:-134.0/centery:31.6/zoom:3')
sleep(5)

popup = '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'
clearPopUp(driver, popup)

#ATRIBUINDO VALOR AO JSON 
ship = response.json()
#num_ship = random.randint(1,len(ship))
sleep(2)
i = 0
#GET DO ID NO JSON PARA REALIZAR A BUSCA
def set_id_ship(vesselJson):
    id_ship = json.dumps(vesselJson[random.randint(1,len(vesselJson))], indent=2)
    print(id_ship)
    data = json.loads(id_ship)
    value_id = data.get('vesselIMONumber')
    return value_id

##FUNÇÃO PARA SELECIONAR UM ELEMENTO RANDOMICO DO JSON RECEBIDO
def jsonVessel(vesselJson):
        value = set_id_ship(vesselJson)
        while value == None:
            value = set_id_ship(vesselJson)
        print('vesselIMONumber ', value)
        return value
##FUNÇÃO DE BUSCA
def searchVessels(driver, par_ship, elementoLista):

    value = jsonVessel(par_ship)
    inptSearch = '//*[@id="searchMarineTraffic"]'
    inptElement = checkElement(driver, inptSearch)

    clickButton(driver, inptSearch, inptElement)
    sleep(2)
    inptSearch = '//*[@id="searchMT"]'
    typeText(driver, inptSearch, value)
    sleep(2)
    #VERIFICAR O E ATRIBUIR O XPATH DA BUSCA
    if elementoLista is None:
        elementolistaClick = '/html/body/div[8]/div[3]/div/div[4]/div[1]/div[2]/div/div/div/div/li/a/div[2]/span'                 
    elif i > 0:
        elementolistaClick = '/html/body/div[7]/div[3]/div/div[4]/div[1]/div[2]/div/div/div/div/li/a/div[2]/span'
    else: 
        elementolistaClick = elementoLista
    elementoListaExiste = checkElement(driver, elementolistaClick)

    if elementoListaExiste:
        if clickButton(driver, elementolistaClick, elementoListaExiste):
            print('NAVIO ENCONTRADO')
            return True
    else:
        print('NAVIO NÃO ENCONTRADO')
        sleep(2)
        ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        searchVessels(driver, ship, '/html/body/div[7]/div[3]/div/div[4]/div[1]/div[2]/div/div/div/div/li/a/div[2]/span/span')
        

busca = searchVessels(driver, ship, None)
print('++++++++++++++++++++++++++++++++++++++', busca)
#LOOP PARA REALIZAR 5 BUSCAS
while i < 5:
    sleep(2)
    elementolistaClick2 = '/html/body/div[8]/div[3]/div/div[4]/div[1]/div[2]/div/div/div/div/li/a/div[2]/span/span'
    searchVessels(driver, ship, elementolistaClick2)
    sleep(3)
    i += 1
print('\n ---------------PESQUISAS FINALIZADAS---------------')
exit()