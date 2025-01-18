# %%
#Diversos
import psutil
import pandas as pd
from IPython.display import clear_output
import ToolBox.kit_function as kit
import ToolBox.login as lg

#WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait

#Ações
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# Exceções
from selenium.common.exceptions import ElementNotInteractableException as NotInteract
from selenium.common.exceptions import ElementClickInterceptedException as NotAvailibleElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException

# %%
def check_Keys():
    try:
        from ToolBox.boxString import keys1,keys2
        return True
    except (ModuleNotFoundError,ImportError):
        print(f'Sem credencial.')
        return False

# %%
def logon_on_site(logon,driver):
    if logon and check_Keys():
        from ToolBox.boxString import keys1,keys2
        driver.get('https://toolsworldb2b.meuspedidos.com.br/entrar')
        lg.Login(driver,keys1,keys2)
    else:
        driver.get('https://toolsworldb2b.meuspedidos.com.br/')
        print(f'Não é possivel realizar o login.')

# %%
logon = True
driver = kit.newWindow()
logon_on_site(logon,driver)

# %%
sheetCategorias = 'Links/CategoriasMTX.xlsx'
columns = ['Link']
categoriasLinks = kit.readExcel(sheetCategorias,columns)

# %%
#Título do Cartão do Produto
cssCategoryTitle = '#catalogWrapper > div:nth-child(2) > div.Catalog__titleB2bContainer___JtAi4 > div > div.Catalog__titleB2bInner___G8ViQ'

#Titulo do produto
clsCardTitle = 'catalog-item-b2b-title'

#Dados do Produto
clsNomeProd = 'ProductInfo__productNameWithAddedToCardIcon___CTBpv'
clsCodProd = 'ProductInfo__productInfo___rlEL5'
clsPrcProd = 'AddToCartContainer__informationForSale___1DaML'
cssMaisInfo = "i[class='materialIcons__materialIcons___NHWaT PopoverPriceDetails__icon___r5kg2 PopoverPriceDetails__container___Gki+K']"
xpathImpostoProd = '/html/body/div[4]/div/ul[4]/li[2]'
cssSeletorMoreItens = "button[class='b2b-button Catalog__links___4450R Catalog__buttonSeeMoreProducts___kZGUm Button__button___Oss6- Button__pointer___mYfJr Button__info___4h9Qg Button__medium___FQv5P Button__buttonInfo___aqiZj custom-brand-full-b2b']"

# %%
def expandMoreItens():
    #----------Scroll----------
    try:
        while True:
            kit.VerifyElement(By.CSS_SELECTOR, cssSeletorMoreItens,driver)
            verProdutos = driver.find_element(By.CSS_SELECTOR, cssSeletorMoreItens)
            verProdutos.click()
    except:
            #print('Verificação Terminada.')
            #Break()
            pass
            
    kit.rollpage(driver,By.TAG_NAME, "footer")

# %%
def navItens(itens,prod,iJump):
    try:
        print('Prox item n°: ' , prod , ' ', itens[prod].text)
        #Centraliza no item
        driver.execute_script("arguments[0].scrollIntoView(true);", itens[prod])
        kit.rollpage(driver,By.TAG_NAME, "footer", -350)
        itens[prod].click()

    except (NotInteract,NotAvailibleElement):
        print('Produto Não Disponivel N°: ', iJump ,'. Incrementando')
        prod += 1
        iJump +=1
        print('Not found:' , itens[prod].text)
        itens[prod].click()
    
    except IndexError:
        print('alow')
        #prod += 1
        #iJump +=1 
    
    return prod,iJump

# %%
init = 0
for posicao, link in enumerate(categoriasLinks['Link'][init:len(categoriasLinks['Link'])], start=init):
    print(f'Posição: {posicao}, Link: {link}')
    driver.get(link)
    
    #----------Captura o título da categoria----------
    titleCategoria = kit.safe_find_element(driver,By.CSS_SELECTOR , cssCategoryTitle).text
    print(titleCategoria)
    expandMoreItens()
    
    #----------Seta a quantidade de itens na pagina----------
    itens = driver.find_elements(By.CLASS_NAME, clsCardTitle)
    print('Total: ' + str(len(itens)) + ' Itens')
    
    #----------Captura dos Dados----------
    nomeList= []
    codList = []
    prcList = []
    impList = []
    prodUrlList = []

    iJump = 0 #Indice de Falha
    prod = 0  #Indíce atual

    #Método para percorrer os itens
    while prod < len(itens):
        #Captura os cards dos itens novamente e clica no item
        itens = driver.find_elements(By.CLASS_NAME, clsCardTitle)
        prod, iJump = navItens(itens,prod,iJump)

        #----------Captura de Dados----------
        nome = kit.safe_find_element(driver, By.CLASS_NAME, clsNomeProd, 'Nome não encontrado')
        cod = kit.safe_find_element(driver, By.CLASS_NAME, clsCodProd, 'Código não encontrado')
        prc = kit.safe_find_element(driver, By.CLASS_NAME, clsPrcProd, "erro")
        try:
            hoverable = driver.find_element(By.CSS_SELECTOR, cssMaisInfo)
            ActionChains(driver).move_to_element(hoverable).perform()
            imp = driver.find_element(By.XPATH, xpathImpostoProd).text
        except:
            imp = "erro"

        if nome == 'Nome não encontrado':
            prod-=1
        else:     
            nomeList.append(nome if isinstance(nome, str) else nome.text)
            codList.append(cod if isinstance(cod, str) else cod.text)
            prcList.append(prc if isinstance(prc, str) else prc.text)
            impList.append(imp)
            prodUrlList.append(driver.current_url)
        
        #Verifica se a memória vai estourar
        memory_percent = psutil.virtual_memory()
        if memory_percent.percent > 95:
            print(f"Falha. Memória RAM: {str(memory_percent.percent)}%")
            driver.quit()   #Fecha o driver
            
            #Reabrir e continuar
            driver = kit.newWindow()
            logon_on_site(logon,driver)
            driver.get(link)    
            expandMoreItens()   
            itens = driver.find_elements(By.CLASS_NAME, clsCardTitle)
            prod +=1 #Salta para o próximo produto
            
        else:
            kit.wait(3)
            prod +=1    
            driver.back()  

    df = {'Nome':nomeList,
        'codigo': codList,
        'prc': prcList,
        'imp': impList,
        'link':prodUrlList}

    xlsx_dir = 'Dados/'

    mtxTable = pd.DataFrame(df)

    file_name = xlsx_dir + titleCategoria + '.xlsx'

    mtxTable.to_excel(file_name, index=False)
    print('Itens da Categoria: ' + titleCategoria + ' Foram salvos')


