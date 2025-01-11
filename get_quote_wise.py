import time

def get_wise(driver):
    driver.get("https://wise.com/br/currency-converter/brl-to-ars-rate?amount=1")
    time.sleep(5)
    input_element = driver.find_element("id", "target-input")
    cotacao = input_element.get_attribute('value').replace(",", ".")
    print(cotacao)
    return float(cotacao)
