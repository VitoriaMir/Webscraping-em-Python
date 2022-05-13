from email import header
import requests

resposta = requests.get('https://www.w3schools.com/')

print('Status code:', resposta.status_code)
print('header') # Vizualização do cabeçalho.

# Permitem que o cliente e o servidor passem informações adicionais com uma solicitação ou resposta HTTP.
print(resposta.headers) 

print(resposta.content) #Vizualização de todo o codigo. 

