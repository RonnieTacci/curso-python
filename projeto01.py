#Jogo de adivinhação

''' No jogo, o usuario precisa advinhar um numero secreto.
    Ele pode tentar varias vezes ate acertar.'''

numero_secreto = 36
tentativa = 0

while tentativa != numero_secreto:
    tentativa = float(input("Tente adivinhar um numero de 1 a 40:"))

    if tentativa < numero_secreto:
        print("O numero secreto é maior.")

    else:
        print("O numero é menor.")    

print("Adivinhou o numero!")
