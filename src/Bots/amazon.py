
def pegarPreco(url):
    from selenium import webdriver
    navegador = webdriver.Chrome()
    navegador.get(url)
    navegador.maximize_window()
    try:
        preco = navegador.find_element("class name", "slot-price").text
        return preco
    except Exception as e:
        print(f"Erro ao pegar o preço: {e}")
        return e
        
print(pegarPreco('https://www.amazon.com.br/Sanduicheira-El%C3%A9trica-Cadence-Click-127V/dp/B0CDJ4L7CZ/ref=zg_bs_c_kitchen_d_sccl_1/145-0320103-4806324'))