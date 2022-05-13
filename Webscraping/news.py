import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://www.w3schools.com/python/default.asp')
conteudo = resposta.content
site = BeautifulSoup(conteudo, 'html.parser')


noticia = site.find('div', class_ = 'w3-panel w3-info intro')

titulo = noticia.find('a', attrs={'class': 'w3-btn w3-margin-bottom'}) # Pode ser assim
print(titulo.text)