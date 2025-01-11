from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def get_nomad(driver):
    driver.get("https://www.nomadglobal.com/cotacoes/peso-argentino")
    time.sleep(5)
    iframe = driver.find_element("class name", "iframe-landing-page")
    driver.switch_to.frame(iframe)
    botao = driver.find_element("xpath", "/html/body/div/div/div/div[1]/button")
    botao.click()
    text = driver.find_element("class name", "ExchangeRate__body-input-static-value")
    valor = text.text.replace(",", ".")
    print(valor)
    return float(valor)
