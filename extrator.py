from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class ExtratorLicitacao:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        prefixo_pregao = "content_content_content_detalhesPregao_"
        self.ids = {
            "organizacao": f"{prefixo_pregao}lblORG",
            "unidade": f"{prefixo_pregao}lblUO",
            "orgao": f"{prefixo_pregao}lblOrgao",
            "processo": f"{prefixo_pregao}lblArea",
            "publicado_em": f"{prefixo_pregao}lblArea",
            "area": f"{prefixo_pregao}lblArea",
            "objeto": f"{prefixo_pregao}lblObjetodaLicitacao",
        }

    def get_attribute(self, attribute):
        return self.driver.find_element(By.ID, self.ids[attribute]).text

    def montar_url_licitacao(self, id):
        url = "http://www.imprensaoficial.com.br"
        detalhe = "/ENegocios/MostraDetalhesLicitacao_14_3.aspx"
        return f"{url}{detalhe}?IdLicitacao={id}"

    def raspar_licitacao(self, url=None, id=None):
        if not url:
            url = self.montar_url_licitacao(id)

        self.driver.get(url)
        print(f"\n - FONTE: {self.driver.title}")
        print(f"\n - URL: {url}")
        print(f"\n - ÁREA: {self.get_attribute('area')}")
        print(f"\n - PUBLICADO EM: {self.get_attribute('publicado_em')}")
        print(f"\n - ORGANIZAÇÃO: {self.get_attribute('organizacao')}")
        print(f"\n - ORGÃO: {self.get_attribute('orgao')}")
        print(f"\n - UNIDADE: {self.get_attribute('unidade')}")
        print(f"\n - PROCESSO: {self.get_attribute('processo')}")
        print(f"\n - OBJETO: {self.get_attribute('objeto')}")
        self.driver.close()


# ExtratorLicitacao().raspar_licitacao(
#     url="http://www.imprensaoficial.com.br/ENegocios/MostraDetalhesLicitacao_14_3.aspx?IdLicitacao=1538690#13/10/2021"
# )

# ExtratorLicitacao().raspar_licitacao(id="1538690")
