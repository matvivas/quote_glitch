from get_quote_wise import get_wise
from get_quote_wu import get_wu
from get_quote_nomad import get_nomad
from selenium import webdriver

bd = []

def preencher_bd(driver):
    global bd
    # Coleta as cotações reutilizando o mesmo navegador
    bd = [
        {"Local": "Wise", "Valor": round(float(get_wise(driver)), 2)},  # Get_wise já retorna float
        {"Local": "Nomad", "Valor": round(float(str(get_nomad(driver)).replace(",", ".")), 2)},  # Verifica se é string e aplica o replace
        {"Local": "WU", "Valor": round(float(get_wu(driver)), 2)},  # Get_wu também retorna float
    ]
    print(bd)
    return bd

def get_wise_cotacao(driver=None):
    return {"Local": "Wise", "Valor": round(float(get_wise(driver)), 2)}

def get_nomad_cotacao(driver=None):
    return {"Local": "Nomad", "Valor": round(float(str(get_nomad(driver)).replace(",", ".")), 2)}

def get_wu_cotacao(driver=None):
    return {"Local": "WU", "Valor": round(float(get_wu(driver)), 2)}
