#Dia 2 - Fábrica de Software - 29/08/2023 - programa capaz de checar se o usuario pode ter uma CNH
num= int(input("Digite a sua idade "))
try:
    if num < 18: #condicional se
        print("Voce pode ter a CNH")
    else: #consequencia
        print("Voce nao pode ter a CNH")
except ValueError:
    raise ValueError ("Voce nao digitou um numero valido")