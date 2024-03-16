from flask import Flask
import requests
from bs4 import BeautifulSoup

def screap():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        headers = {
            'User-Agent'        : 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
            'Accept'            : '*/*',
            'Accept-Language'   : 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'DNT'               : '1',
            'Connection'        : 'close'

        }

        link = 'https://www.fundamentus.com.br/resultado.php'

        try:
            requisicao = requests.get(link, headers=headers, timeout=5).text
            soup = BeautifulSoup(requisicao, "html.parser")
            table = str(soup.find('table'))

            return table
        except RecursionError:
            print("\nFalha na Requisição\n")
            return ""
    
    return app
