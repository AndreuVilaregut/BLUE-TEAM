from funcions.info_ip import consultar_ip
from textos.textos import titol, menu_principal, text_opcio, text_ip
from textos.errors import error_valor_incorrecte, error_ip

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

def info_url():
    print("Funcionalitat pendent d'implementar.")

def info_domini():
    print("Funcionalitat pendent d'implementar.")

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
            info_url()
        elif opcio == 3:
            info_domini()
        else:
            print(error_valor_incorrecte())

if __name__ == "__main__":
    titol()
    main()
