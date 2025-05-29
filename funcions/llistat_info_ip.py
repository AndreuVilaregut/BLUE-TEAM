import csv
import requests
import time
from os import path
from textos.textos import taula_ip_info
from colorama import Fore
from textos.errors import error_ip, error_fitxer_no_existeix

def consultar_llistat_ips(csv_path):
    if not path.isfile(csv_path):
        print(error_fitxer_no_existeix())
        return

    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Accept': 'application/json',
        'Key': 'bfdde48b7e57f01916e48e5b36f8e79aa133ebff554b2ccb264e8e7215b6bca71eb33adec5e2ef93'
    }

    resultats = []

    try:
        with open(csv_path, newline='') as csvfile:
            lector = csv.reader(csvfile)
            for fila in lector:
                if not fila:
                    continue
                ip = fila[0].strip()
                querystring = {'ipAddress': ip, 'maxAgeInDays': '90'}

                try:
                    response = requests.get(url, headers=headers, params=querystring)
                    data = response.json()

                    if 'data' in data:
                        ip_data = data['data']
                        resultats.append({
                            'ip': ip_data.get('ipAddress', 'N/D'),
                            'country': ip_data.get('countryCode', 'N/D'),
                            'isp': ip_data.get('isp', 'N/D'),
                            'domain': ip_data.get('domain', 'N/D'),
                            'score': ip_data.get('abuseConfidenceScore', 0)
                        })
                    else:
                        print(error_ip(ip))
                except Exception:
                    print(error_ip(ip))

                time.sleep(1)

    except FileNotFoundError:
        print(error_ip())
        return

    resultats.sort(key=lambda x: x['score'], reverse=True)

    for ip_info in resultats:
        print(taula_ip_info(
            ip=ip_info['ip'],
            country=ip_info['country'],
            isp=ip_info['isp'],
            domain=ip_info['domain'],
            score=ip_info['score']
        ))
