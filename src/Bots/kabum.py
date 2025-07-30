class robo:
    def pegarPreco(url):
        from selenium import webdriver
        navegador = webdriver.Chrome()
        navegador.get(url)
        try:
            preco = navegador.find_element("text-4xl text-secondary-500 font-bold transition-all duration-500").text
            return preco
        except Exception as e:
            print(f"Erro ao pegar o preço: {e}")
            return e