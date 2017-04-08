import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4
from PIL import Image
from pytesseract import image_to_string

DNI = '46238982'

URL_RAIZ = 'http://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/'

sesion = requests.Session()
imagen_response = sesion.get(URL_RAIZ + 'captcha?accion=image')
archivo = open('imagen.jpg', 'wb')
archivo.write(imagen_response.content)
archivo.close()
captcha = image_to_string(Image.open('imagen.jpg'))
print('Captcha: {}'.format(captcha))

formulario = {
    'accion': 'consPorTipdoc',
    'razSoc': '',
    'nroRuc': '',
    'nrodoc': DNI,
    'contexto': 'ti-it',
    'search1': '',
    'codigo': captcha,
    'tQuery': 'on',
    'tipdoc': '1',
    'search2': DNI,
    'coddpto': '',
    'codprov': '',
    'coddist': '',
    'search3': ''
}

response = sesion.post(URL_RAIZ + 'jcrS00Alias', data=formulario)
soup = BeautifulSoup(response.content, 'html.parser')
resultados = [elemento.text for elemento
              in soup.find_all(attrs={'class': 'bg'})]

print(''.join(resultados))
