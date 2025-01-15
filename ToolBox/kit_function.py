# %%
import time
#Função para aguardar o tempo em Segundos
def wait(timeClock):
    """Aguarda um tempo especifico

    Args:
        timeClock (number): Em Segundos
    """
    timeClock
    time.sleep(timeClock)

# %%
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait



def VerifyElement(by_type, identifier,driver):
    """Verifica se o elemento existe e o aguarda caso não esteja aparecendo

    Args:
        by_type (_type_): By.CLASS_NAME , By.TAG_NAME ,  By.XPATH , By.ID
        identifier (_type_): str do elemento

    Returns:
        _None
    """
    try:
        print('Esperando Elemento...')
        # Esperar até que o elemento esteja presente
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by_type, identifier))
        )
        # Agora você pode interagir com o elemento
        print("Elemento encontrado!!!")
        return element
    except (TimeoutException , NoSuchElementException):
        print("O tempo de espera para o elemento expirou.")
        return None

# %%
import pandas as pd 
def readExcel(pathExcel,arrColumns):
    """
    Lê um arquivo Excel e retorna um DataFrame contendo apenas as colunas especificadas.

    Parâmetros:
    pathExcel (str): O caminho para o arquivo Excel que será lido.
    arrColumns (list): Lista com os nomes das colunas que devem ser carregadas do arquivo Excel.

    Retorna:
    pd.DataFrame: Um DataFrame contendo apenas as colunas especificadas pelo parâmetro `arrColumns`.
    
    # Lendo o arquivo do excel
    pathExcel = './excel/links_produtos_tigre.xlsx'
    columns = ['Links']
    arr_links_tigre = kit_function.readExcel(pathExcel, columns)

    Exemplo:
    >>> df = readExcel('dados.xlsx', ['Nome', 'Idade'])
    >>> print(df)
       Nome  Idade
    0  Ana     30
    1  João    25
    """
    df = pd.read_excel(pathExcel, usecols=arrColumns)
    return df

# %%
def readTXT(pathfile,array):
    """
    Lê um arquivo de texto e adiciona cada linha a uma lista fornecida.

        Esta função abre o arquivo especificado pelo caminho `pathfile`, lê seu conteúdo linha por linha,
        remove espaços em branco e quebras de linha das extremidades de cada linha, e adiciona cada linha 
        processada à lista `array`. Após a leitura completa do arquivo, a função imprime a quantidade total 
        de linhas (links) adicionadas à lista.

        Parâmetros:
        pathfile (str): Caminho para o arquivo de texto que será lido.
        array (list): Lista onde cada linha do arquivo será adicionada.

        Retorna:
        None

        Exemplo:
        >>> links = []
        >>> readTXT('links.txt', links)
        Lendo o arquivo: links.txt
        Quantidade de links no arquivo: 10
    """
    
    # Abrir e ler o arquivo linha por linha
    with open(pathfile, 'r') as file:
        print(f'Lendo o arquivo: {pathfile}')
        for line in file:
            # Processar a linha (aqui estamos apenas imprimindo)
            link = line.strip()
            array.append(link)
            #print(link)
    print(f'Quantidade de links no arquivo : {len(array)}')

# %%
def append_dict(titles, content, dictionary):
    """
    Adiciona títulos e variáveis a um dicionário de dados.

    Args:
        titles (list): Lista de títulos a serem usados como chaves no dicionário.
        content (list): Lista de variáveis correspondentes aos títulos.
        dictionary (dict): Dicionário onde os dados serão armazenados.

    Retorna:
        dict: O dicionário atualizado com os novos dados.
    """
    for title, var in zip(titles, content):
        dictionary[title].append(var if var is not None else 'Nulo')
        print(f'Adicionado {title} no dict de Dados: {var}')
    #return dictionary