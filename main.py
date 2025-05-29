from idlelib.autocomplete import FORCE

from funcions.info_ip import consultar_ip
from funcions.llistat_info_ip import consultar_llistat_ips
from textos.textos import titol, menu_principal, text_opcio, text_ip, ruta_csv
from textos.errors import  error_ip, error_fitxer_no_existeix, error_valor_incorrecte
from colorama import Fore, Style, init

init(autoreset=True)

def info_ip():

    while True:
        try:
            ip = input(text_ip())

            if ip.strip() == "0":
                break

            consultar_ip(ip)
        except KeyboardInterrupt:
            print(error_ip())
            break

def llistat_info_ip():
    while True:
        try:
            ruta = input(Fore.LIGHTCYAN_EX + Style.BRIGHT + ruta_csv())

            if ruta.strip() == "0":
                break

            consultar_llistat_ips(ruta)
        except KeyboardInterrupt:
            print(error_valor_incorrecte())
            break

def main():
    while True:
        menu_principal()
        try:
            opcio = int(input(text_opcio()))
        except ValueError:
            print(error_valor_incorrecte())
            continue

        if opcio == 0:
            print("Sortint del programa...")
            break
        elif opcio == 1:
            info_ip()
        elif opcio == 2:
            llistat_info_ip()
        else:
            print(error_valor_incorrecte())

if __name__ == "__main__":
    titol()
    main()
