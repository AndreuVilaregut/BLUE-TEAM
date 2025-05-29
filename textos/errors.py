from colorama import Fore, Style

def error_fitxer_no_existeix():
    return (
        Fore.RED + Style.BRIGHT +
        "=========================================================\n"
        "❌ ERROR: El fitxer especificat no existeix.\n"
        "========================================================="
    )

def error_ip(ip):
    return (
        Fore.RED + Style.BRIGHT +
        "=========================================================\n"
        f"⚠️  ERROR: No s'ha pogut obtenir informació per a la IP {ip}\n"
        "========================================================="
    )

def error_valor_incorrecte():
    return (
        Fore.LIGHTRED_EX + Style.BRIGHT +
        "=========================================================\n"
        "NO HAS INTRODUIT UN VALOR CORRECTE!\n"
        "========================================================="
    )

