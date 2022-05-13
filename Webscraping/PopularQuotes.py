import requests
from bs4 import BeautifulSoup

def popular():
    pagina = requests.get('https://www.goodreads.com/quotes')
    soup = BeautifulSoup(pagina.content, 'html.parser')
    divs = soup.find_all('div', class_='quoteText')
    autor = soup.find_all('div', class_='authorOrTitle')
    frases = []
    
    for elemento in divs:

        lista_elemento = elemento.text.split('―')
        frase = lista_elemento[0].replace('\n', '').strip()
        autor = lista_elemento[1].replace('\n', '').strip()
        #frases.append(elemento.text)
        frases.append({"FRASE:":frase, "AUTOR:":autor})
        #print(frase, autor)
    print(frases)

popular()