
def pegarPreco(url):
    from selenium import webdriver
    navegador = webdriver.Chrome()
    navegador.get(url)
    navegador.maximize_window()
    try:
        preco = navegador.find_element("class name", "andes-money-amount__fraction").text
        return preco
    except Exception as e:
        print(f"Erro ao pegar o preço: {e}")
        return e

