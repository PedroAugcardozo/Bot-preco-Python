class robo:
    def pegarPreco(url):
        from selenium import webdriver
        navegador = webdriver.Chrome()
        navegador.get(url)
        try:
            preco = navegador.find_element("class_name", "slot-price").text
            return preco
        except Exception as e:
            print(f"Erro ao pegar o preço: {e}")
            return e