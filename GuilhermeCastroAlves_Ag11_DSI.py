#Utilizar o colorama
from colorama import Fore, init
init(autoreset=True)

# Lista dos níveis
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para definir a cor
def definir_cor(nivel):
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
# Retorna a cor correspondente
    return cores[nivel - 1]

# Loop para mostrar os níveis
for i, texto in enumerate(niveis, start=1):
    cor = definir_cor(i)
    print(cor + f"Nível {i}: {texto}")