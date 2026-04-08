#Peça um numero e diga se ele é par ou impar


num = int(input("Digite um numero: "))

if num % 2 == 0:            # (% -> pega o resto da divisão)
    print("Par")
else:
    print("Impar")

