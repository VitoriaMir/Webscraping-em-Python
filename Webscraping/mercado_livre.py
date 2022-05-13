""" > EXEMPLO
- Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário
"""

from urllib import response
import requests
from bs4 import BeautifulSoup

url = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')
resposta = requests.get(url + produto_nome)
site = BeautifulSoup(resposta.text, 'html.parser')

produto = site.findAll('div', attrs={'class': 'ui-search-result__content-wrapper'})

for produtos in produto:

    titulo = produtos.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produtos.find('a', attrs={'class': 'ui-search-link'})

    real = produtos.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produtos.find('span', attrs={'class': 'price-tag-cents'})

    #print(produtos.prettify())
    print('Titulo do produto:', titulo.text)
    print('Link do produto:', link['href'])

    if (centavos):
        print('Preço do produto: R$', real.text + ',' + centavos.text)
    else:
        print('Preço do produto: R$', real.text + ',00')

    print('\n\n')

