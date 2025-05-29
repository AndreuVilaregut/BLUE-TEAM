import requests
from textos.textos import taula_ip_info
from textos.errors import error_ip

def consultar_ip(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'bfdde48b7e57f01916e48e5b36f8e79aa133ebff554b2ccb264e8e7215b6bca71eb33adec5e2ef93'
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    if 'data' in data:
        ip_data = data['data']
        print(taula_ip_info(
            ip=ip_data.get('ipAddress', 'N/D'),
            country=ip_data.get('countryCode', 'N/D'),
            isp=ip_data.get('isp', 'N/D'),
            domain=ip_data.get('domain', 'N/D'),
            score=ip_data.get('abuseConfidenceScore', 0)
        ))
    else:
        print(error_ip(ip))
