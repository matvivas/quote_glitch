import time

def get_wu(driver):
    driver.get("https://www.westernunion.com/br/pt/currency-converter/brl-to-ars-rate.html")
    time.sleep(5)
    texto = driver.find_element("xpath", "/html/body/div[2]/section[1]/section[1]/div/div/div/div[3]/div[4]/div/p/strong/span")
    cotacao = texto.text
    valor_numerico = cotacao.split()[0].replace(",", ".")
    return round(float(valor_numerico), 2)

