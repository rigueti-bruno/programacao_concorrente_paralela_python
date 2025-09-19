# Modulo para obter os simbolos do S&P 500 da Wikipedia:
import requests
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies " # URL da pagina da Wikipedia
        
    def get_sp_500_companies(self):
        response = request.get(self._url) # Faz a requisicao HTTP para obter o conteudo da pagina
        
        if response.status_code != 200:
            print("Couldn't get entries")
            return []
        
    def _extract_company_symbols(self,page_html):
        soup = BeautifulSoup(page_html)
        table = soup.find(id='constituents') # Encontra a tabela com os simbolos das empresas
        table_rows = table.find_all('tr') # Encontra todas as linhas da tabela
        for table_row in table_rows[1:]: # Ignora a primeira linha (cabeçalho)
            symbol = table_row.find('td').text.strip('\n') # Extrai o simbolo da empresa
            yield symbol # Retorna o simbolo como um gerador

        yield from self._extract_company_symbols(response.text) # Extrai os simbolos das empresas da pagina HTML