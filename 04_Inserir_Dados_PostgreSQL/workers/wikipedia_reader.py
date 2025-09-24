# Modulo para obter os simbolos do S&P 500 da Wikipedia:
import requests
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies" # URL da pagina da Wikipedia
    
    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents') # Encontra a tabela com os simbolos das empresas
        table_rows = table.find_all('tr') # Encontra todas as linhas da tabela
        #symbols = []
        for table_row in table_rows[1:]: # Ignora a primeira linha (cabeçalho)
            symbol = table_row.find('td').text.strip() # Extrai o simbolo da empresa
            symbol = symbol.replace('.','-') # Substitui pontos por hifens (Yahoo Finance usa hifens)
            #symbols.append(symbol)
        #yield from symbols # Retorna os simbolos como um gerador
            yield symbol
            
    def get_sp_500_companies(self):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        response = requests.get(self._url, headers=headers) # Faz a requisicao HTTP para obter o conteudo da pagina
        if response.status_code != 200:
            print("Couldn't get entries")
            return [] 
        
        yield from self._extract_company_symbols(response.text) # Extrai os simbolos das empresas da pagina HTML