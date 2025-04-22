from colorama import Fore, Style, init

init(autoreset=True)

def titol():
    lines = [
        " ____  _    _   _ _____   _____ _____    _    __  __ ",
        "| __ )| |  | | | | ____| |_   _| ____|  / \\  |  \\/  |",
        "|  _ \\| |  | | | |  _|     | | |  _|   / _ \\ | |\\/| |",
        "| |_) | |__| |_| | |___    | | | |___ / ___ \\| |  | |",
        "|____/|_____\\___/|_____|   |_| |_____/_/   \\_\\_|  |_|",
        "",
    ]
    for line in lines:
        print(Fore.BLUE + Style.BRIGHT + line)

def menu_principal():
    lines = [
        (Fore.LIGHTYELLOW_EX + Style.BRIGHT, "---------------------------------------------------------"),
        (Fore.LIGHTCYAN_EX + Style.BRIGHT,   "1. CONSULTAR UNA IP"),
        (Fore.LIGHTMAGENTA_EX + Style.BRIGHT,"2. CONSULTAR UNA URL"),
        (Fore.LIGHTBLUE_EX + Style.BRIGHT,   "3. CONSULTAR UN DOMINI"),
        (Fore.LIGHTYELLOW_EX + Style.BRIGHT, "---------------------------------------------------------"),
    ]
    for color, line in lines:
        print(color + line)


def text_opcio():
    return (
        Fore.LIGHTWHITE_EX + Style.BRIGHT +
        "---------------------------------------------------------\n"
        "INTRODUEIX LA ACCIÓ QUE VOLS REALITZAR:\n"
        "---------------------------------------------------------\n> "
    )

def text_ip():
    return (
        Fore.LIGHTCYAN_EX + Style.BRIGHT +
        "---------------------------------------------------------\n"
        "INTRODUEIX LA IP QUE VOLS CONSULTAR:\n"
        "---------------------------------------------------------\n> "
    )

def taula_ip_info(ip, country, isp, org):
    return (
        Fore.LIGHTGREEN_EX + Style.BRIGHT +
        "---------------------------------------------------------\n"
        f"| {'DADA':<10} | {'VALOR':<40}|\n"
        "---------------------------------------------------------\n"
        f"| {'IP':<10} | {ip:<40}|\n"
        f"| {'País':<10} | {country:<40}|\n"
        f"| {'ISP':<10} | {isp:<40}|\n"
        f"| {'Empresa':<10} | {org:<40}|\n"
        "---------------------------------------------------------"
    )
