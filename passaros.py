from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from openpyxl import Workbook
from time import sleep

driver = Chrome()
driver.get('https://turismodenatureza.com.br/passaros-mais-bonitos-do-brasil/')
sleep(2)
dados = []

passaros = driver.find_elements(By.XPATH, '//div[2]/main/div/div[1]/div[5]/div/h3')
    
for i, dado in enumerate(passaros):
    dados.append(dado.text.replace(f'{i+1} – ', '').capitalize())

arquivo = Workbook()
pagina = arquivo.active
pagina.title = 'Passaros - results'
pagina['A1'] = 'ID'
pagina['B1'] = 'NOME'
for indice, resultado in enumerate(dados):
    pagina[f'A{indice+2}'] = indice+1
    pagina[f'B{indice+2}'] = resultado
    
arquivo.save('Passaros-Selenium.xlsx')
