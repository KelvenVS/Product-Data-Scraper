<div align="center">
<h1 style="font-weight: bold;">Product Data Scraper 🚀</h1>

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.27.1-green?style=for-the-badge&logo=selenium)
![Pandas](https://img.shields.io/badge/Pandas-v2.2.3-yellow?style=for-the-badge&logo=pandas)
![psutil](https://img.shields.io/badge/Psutil-v6.1.1-orange?style=for-the-badge&logo=python)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1.5-purple?style=for-the-badge&logo=python)

</div>

<p align="center">

  • [Introdução](#introdução) • [Descrição](#descrição) • [Funcionalidades](#funcionalidades) • [Estrutura do Projeto](#estrutura-do-projeto) • [Dependências](#dependências) • [Instalação](#instalação) • [Como Usar](#como-usar) • [Limpeza e Formatação de Dados (Em Desenvolvimento)](#Limpeza-e-Formatação) • [Sobre o Autor](#sobre-o-autor) • [Licença](#licença)

</p>

## Introdução

O **Product Data Scraper** é um conjunto de scripts em Python que automatiza a coleta de dados de produtos a partir de um site. Ele opera em duas etapas principais: 

1. **Captura de Categorias**: Um script inicial coleta os links das categorias de produtos disponíveis no site e salva-os em um arquivo Excel.
2. **Extração de Dados de Produtos**: O segundo script utiliza os links capturados para acessar e extrair informações detalhadas sobre os produtos.

Essa abordagem modular facilita a automação em grande escala e permite um controle mais eficiente do fluxo de dados.

![Captura dos produtos de uma categoria](<images/funcionamento.gif>)


## Descrição

Na primeira etapa, o script de captura de categorias utiliza o Selenium para navegar em um site específico e identificar os links das categorias. Esses links são salvos em um arquivo Excel, que serve como ponto de partida para o próximo script de scraping.

Na segunda etapa, outro script consome os links das categorias e realiza o scraping detalhado dos produtos, incluindo informações como nome, código, preço e impostos.

Você pode executar e depurar o código utilizando Jupyter Notebook ou diretamente no Python.

### Tecnologias Utilizadas

- **Python 3.10**
- **Selenium WebDriver** para automação de navegação.
- **Pandas** para manipulação de dados e geração de arquivos Excel.
- **Psutil** para monitoramento de uso de memória.
- **IPython** para interação avançada e debug.

## Funcionalidades

### Etapa 1: Captura de Categorias
- **Navegação Automatizada**:
  - Acessa o site especificado e identifica as categorias de produtos disponíveis.
- **Exportação Estruturada**:
  - Salva os links das categorias em um arquivo Excel para uso posterior.

### Etapa 2: Extração de Dados de Produtos
- **Navegação Automatizada**:
  - Acessa links de categorias fornecidos via arquivo Excel.
  - Expande automaticamente listas de produtos nas páginas.
- **Coleta de Dados**:
  - Nome do produto, código, preço, impostos e links individuais.
  - Suporte a múltiplas categorias.
- **Salvamento Estruturado**:
  - Exporta os dados coletados para arquivos Excel separados por categoria.
- **Gerenciamento de Recursos**:
  - Monitora o uso de memória RAM e reinicia o WebDriver quando necessário.

### Sobre o kit_function

O `kit_function` é um conjunto de funções utilitárias desenvolvidas para facilitar a automação de tarefas com o Selenium e manipulação de arquivos. Ele inclui funções para aguardar a presença de elementos em uma página web, ler e processar arquivos Excel e TXT, além de facilitar a manipulação de dados e interações com o navegador.

#### Funções do kit:

- `wait(timeClock)`: Aguarda um tempo específico em segundos antes de continuar a execução do script.
- `VerifyElement(by_type, identifier, driver)`: Verifica se um elemento existe na página, aguardando até que ele seja encontrado.
- `readExcel(pathExcel, arrColumns)`: Lê um arquivo Excel e retorna um DataFrame contendo apenas as colunas especificadas.
- `readTXT(pathfile, array)`: Lê um arquivo de texto linha por linha e adiciona cada linha a uma lista.
- `append_dict(titles, content, dictionary)`: Adiciona títulos e valores a um dicionário de dados, garantindo que dados nulos sejam tratados.
- `rollpage(driver, by_type, identifier, step)`: Rola a página de um site para baixo ou para cima, em uma quantidade específica de pixels, facilitando a navegação em páginas longas.
- `safe_find_element(driver, by, identifier, default_value=None)`: Tenta localizar um elemento na página, retornando um valor padrão caso o elemento não seja encontrado.
- `newWindow()`: Cria uma nova instância do navegador Edge para ser usada no processo de scraping.

## Estrutura do Projeto

```plaintext
src/
├── CapturaDosProdutos.py   # Script que captura os detalhes dos produtos
├── CapturaDasCategorias.py   # Script que captura as categorias
├── ToolBox/
│   ├── kit_function.py     # Funções auxiliares para manipulação de elementos e dados
│   ├── login.py            # Automação de login no site
│   └── boxString.py        # Credenciais e strings sensíveis
├── Dados/                  # Diretório de saída para arquivos Excel gerados
└── Links/
    └── CategoriasMTX.xlsx  # Arquivo com links das categorias
```

## Dependências
As bibliotecas principais utilizadas no projeto são:

- Selenium: 4.27.1
- Pandas: 2.2.3
- Psutil: 6.1.1
- IPython: 8.31.0
- Openpyxl 3.1.5

## Como Usar

### Etapa 1: Captura de Categorias

1. Execute o script:
```bash
python CapturaDasCategorias.ipynb
```

2. Após a execução, o arquivo `CategoriasMTX.xlsx` será salvo no diretório `Links/`, contendo os links das categorias disponíveis.

```markdown
| Link                               |
|------------------------------------|
| https://example.com/categoria/001  |
| https://example.com/categoria/002  |
```

### Etapa 2: Extração de Dados de Produtos

1. Configure o arquivo `CategoriasMTX.xlsx` no diretório `Links/` com os links das categorias que deseja capturar.

2. Execute o script principal:
```bash
python CapturaDosProdutos.py
```

3. O script abrirá um navegador automatizado para acessar os links e capturar os dados.

4. Os resultados serão salvos em arquivos Excel no diretório `Dados/`.

## Limpeza e Formatação
### Desenvolvimento

A parte de limpeza e formatação de dados do projeto está em andamento. O código realiza a limpeza de informações extraídas, aplicando expressões regulares para identificar e extrair dados específicos, como códigos de produtos, preços e tributações (IPI e ST).

### O que está em desenvolvimento:

- `Extração de Dados`: Utiliza expressões regulares para identificar padrões como códigos numéricos e valores monetários (R$).
- `Formatação de Preços e Impostos`: Está sendo implementado um processo para formatar corretamente os preços, valores de IPI e ST.

## Sobre o Autor

*Este projeto foi desenvolvido por **Kelven Vilela Serejo**, utilizando Python e Selenium para automação e scraping de dados. O objetivo principal é simplificar e otimizar a captura de informações de produtos em catálogos online.*

## Aviso

*Este projeto foi desenvolvido exclusivamente para fins de estudo e aprendizado. Não há garantia de funcionamento em ambientes de produção ou suporte técnico. Use por sua conta e risco.*

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](./LICENSE.md) para mais detalhes.