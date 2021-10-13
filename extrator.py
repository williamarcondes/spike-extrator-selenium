from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('http://www.imprensaoficial.com.br/ENegocios/MostraDetalhesLicitacao_14_3.aspx?IdLicitacao=1538690#13/10/2021')


print('\n\nTITÚLO:')
print(driver.title)


print('\n\nURL:')
print(driver.current_url)

area = driver.find_element(By.ID, 'content_content_content_detalhesPregao_lblArea').text
print('\n\nÁREA')
print(area)

objeto = driver.find_element(By.ID, 'content_content_content_detalhesPregao_lblObjetodaLicitacao').text
print('\n\nObjeto:')
print(objeto)

driver.close()