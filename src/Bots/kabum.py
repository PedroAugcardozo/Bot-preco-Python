from selenium.webdriver.chrome.options import Options

def pegarPreco(url):
    from selenium import webdriver
    navegador = webdriver.Chrome()
    navegador.get(url)
    options = Options()
    options.add_argument("--headless")            # Oculta a janela
    options.add_argument("--disable-gpu")         # Evita problemas gráficos
    options.add_argument("--window-size=1920,1080")  # Tamanho da tela virtual
    options.add_argument("--no-sandbox")          # Evita erros em alguns ambientes Linux
    options.add_argument("--disable-dev-shm-usage")
    try:
        preco = navegador.find_element("class name","text-4xl text-secondary-500 font-bold transition-all duration-500").text
        return preco
    except Exception as e:
        print(f"Erro ao pegar o preço: {e}")
        return e