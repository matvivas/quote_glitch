from flask import Flask, render_template, redirect, url_for, jsonify
from selenium import webdriver
from bd import preencher_bd, get_wise_cotacao, get_nomad_cotacao, get_wu_cotacao

app = Flask(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("detach", True)  # Mantém o navegador aberto
    options.add_argument("--start-maximized")        # Abre o navegador em tela cheia
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(options=options)
    return driver

@app.route('/', methods=['GET'])
def cotacao():
    driver = get_driver()  # Cria uma nova instância do driver
    cotacoes = preencher_bd(driver)  # Coleta as cotações
    cotacoes = sorted(cotacoes, key=lambda x: x['Valor'])
    driver.quit()  # Fecha o navegador após obter as cotações
    return render_template('index.html', cotacoes=cotacoes)

@app.route('/wise', methods=['GET'])
def wise_cotacao():
    driver = get_driver()
    wise = get_wise_cotacao(driver)
    driver.quit()  
    return jsonify(wise)

@app.route('/nomad', methods=['GET'])
def nomad_cotacao():
    driver = get_driver()
    nomad = get_nomad_cotacao(driver)
    driver.quit() 
    return jsonify(nomad)

@app.route('/wu', methods=['GET'])
def wu_cotacao():
    driver = get_driver()
    wu = get_wu_cotacao(driver)
    driver.quit() 
    return jsonify(wu)

if __name__ == '__main__':
    app.run(debug=True)
