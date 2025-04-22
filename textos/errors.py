from colorama import Fore, Style, init

init(autoreset=True)

def error_valor_incorrecte():
    return (
        Fore.LIGHTRED_EX + Style.BRIGHT +
        "---------------------------------------------------------\n"
        "NO HAS INTRODUIT UN VALOR CORRECTE!\n"
        "---------------------------------------------------------"
    )

def error_ip():
    return (
        Fore.LIGHTRED_EX + Style.BRIGHT +
        "---------------------------------------------------------\n"
        "NO S'HA POGUT OBTENIR INFOMRACIÓ SOBRE AQUESTA IP!\n"
        "---------------------------------------------------------"
    )
