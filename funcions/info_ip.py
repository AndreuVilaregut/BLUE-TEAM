import requests
from colorama import Fore, Style
from textos.textos import taula_ip_info
from textos.errors import error_ip

def consultar_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print(taula_ip_info(
            ip=data['query'],
            country=data['country'],
            isp=data['isp'],
            org=data['org']
        ))
    else:
        print(error_ip())
