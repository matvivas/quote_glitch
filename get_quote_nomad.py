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
    valor_final = valor.replace(" ", "")
    print(valor_final)
    return float(valor)
