#CONDICIONAIS

'''São estruturas que permitem ao nosso programa tomar decisões
com base em determinadas condições. O programa executa ações 
diferentes dependendo de uma situação especifica.'''

#Exemplo:

'''Estou em uma cafeteria e estou com pouco dinheiro.
O cappucino custa 10 reais, café com leite 7 e o café simples 4.

SE eu tiver 10 reis ou mais (>=), posso pedir cappuccino
SE eu tiver 7 reais ou mais, possopedir café com leite
SE NÃO, pede o café simples.'''

#Exemplo:  (if, elif e else)

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Permissão para jogar lol")

else:
    print("Caiu na lei Felca, volte quando tiver idade adequada. ")