# %%
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from IPython.display import clear_output
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import ToolBox.kit_function as kit
from openpyxl import load_workbook

# %%
# Inicializa a instância do EDGE
service = Service()

options = webdriver.EdgeOptions()
options.add_argument("-inprivate")
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()

url = 'https://toolsworldb2b.meuspedidos.com.br/'

driver.get(url)
kit.wait(10)

# %%
dados_tabela = {'Link' : []}

# %%
css_refTigre = '#__nuxt > div > div.layout > main > div > section:nth-child(2) > div > div > div.col-md-5.col-lg-6.col-xxl-5.offset-xxl-1 > div > div.mt-4.mt-sm-0.mb-6 > div > h1'

seletor_Categorias1 = 'Categories__container___GNWEE'

# %%
# Espera Elemento
kit.VerifyElement(By.CLASS_NAME, seletor_Categorias1,driver)
# Classe Mestre das Categorias
refCat1 = driver.find_element(By.CLASS_NAME, seletor_Categorias1)
# Subclasse das categorias
refCat2 = refCat1.find_elements(By.TAG_NAME , 'a')

# %%
#Adiciona os links em um Dicionário
for element in refCat2:
    link = element.get_attribute('href')
    #print(link)
    dados_tabela['Link'].append(link)

# %%
#Cria uma planilha em XLSX para armazenar os links
xlsx_dir = 'Links'
xlsx_name = 'CategoriasMTX'
tableGenerate = pd.DataFrame(dados_tabela)
file_name = xlsx_dir + '/' + xlsx_name + '.xlsx'
tableGenerate.to_excel(file_name, index=False)


