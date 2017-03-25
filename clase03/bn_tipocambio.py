import re
import requests
from bs4 import BeautifulSoup

response = requests.get('https://zonasegura1.bn.com.pe/TipoCambio/')
soup = BeautifulSoup(response.content, 'html.parser')
cambio = soup.find_all('ul')[1].text
compra, venta, impuesto = re.findall(r'\d+\.\d+', cambio)

print('compra: {}'.format(compra))
print('venta: {}'.format(venta))
print('impuesto: {}'.format(impuesto))
