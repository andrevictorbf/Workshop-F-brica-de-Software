#Medidor de velocidade e aplicador de multas - exercicio Fabrica - 29/08/2023
num= int(input("Digite a velocidade "))
try: #condicional - testa se há a velocidade permitida ou nao
    if num > 80: #velocidade permitida - 80km/h
        print(f"Voce foi multado. Velocidade de {num} a multa sera de {(num -80)*7}")
    else: #velocidade permitida
        print("Velocidade permitida")
except ValueError:
    raise ("Voce nao digitou um numero inteiro")