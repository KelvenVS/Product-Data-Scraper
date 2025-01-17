import ToolBox.kit_function as kit
from selenium.webdriver.common.by import By

def Login(driver,key1,key2):
    xpathEmail = "//input[@placeholder='E-mail']"
    entrar = kit.safe_find_element(driver, By.XPATH, xpathEmail)
    entrar.click()
    entrar.send_keys(key1)

    xpathSenha = "//input[@placeholder='Senha']"
    senha = kit.safe_find_element(driver, By.XPATH, xpathSenha)
    senha.click()
    senha.send_keys(key2)

    xpathBtnLogin = "//button[@type='submit']"
    btnlg = kit.safe_find_element(driver, By.XPATH, xpathBtnLogin)
    btnlg.click()
    
    kit.wait(10)