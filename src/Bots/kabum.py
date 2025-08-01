
def pegarPreco(url):
    from selenium import webdriver
    navegador = webdriver.Chrome()
    navegador.get(url)
    navegador.maximize_window()
    try:
        preco = navegador.find_element("class name","text-4xl text-secondary-500 font-bold transition-all duration-500").text
        return preco
    except Exception as e:
        print(f"Erro ao pegar o preço: {e}")
        return e
print(pegarPreco('https://www.kabum.com.br/produto/165133/placa-mae-asus-tuf-gaming-a520m-plus-ii-amd-am4-matx-ddr4-preto-90mb17g0-m0eay0'))