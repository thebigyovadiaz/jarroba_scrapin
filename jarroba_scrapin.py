# -*- coding: utf8 -*-
__autor__ = 'Yovanny Diaz'

from bs4 import BeautifulSoup
import requests

URL_BASE = "http://jarroba.com/"
MAX_PAGES = 20
counter = 0

for i in range(1, MAX_PAGES):
    # Se construye la url
    if i > 1:
        url = "{0}page/{1}".format(URL_BASE, i)
    else:
        url = URL_BASE

    # Petición HTTP
    req = requests.get(url)
    # Se comprueba status code 200
    status_code = req.status_code
    if status_code == 200:
        # Contenido HTML a BeatifulSoup
        html = BeautifulSoup(req.text, "html.parser")

        # Se obtienen los divs
        divs = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

        # Se recorren los divs para extraer data necesaria
        for div in divs:
            counter += 1
            titulo = div.find('span', {'class': 'tituloPost'}).getText()
            autor = div.find('span', {'class': 'autor'}).getText()
            fecha = div.find('span', {'class': 'fecha'}).getText()

            print('{0} - {1} | {2} | {3}'.format(counter, titulo, autor, fecha))

    else:
        # Sino existe la página retorna 404
        break
