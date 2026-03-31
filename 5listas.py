# LISTAS E TUPLAS

#Tipos de dados que armazenam multiplos valores

'''LISTAS:

- Modificavel(pode adicionar, remover e alterar valores)
- Mais lenta
- Boa para quando precisamos modificar dados'''

'''Tuplas:

- Não pode ser modificada/alterada apos a criação!
- Mais rapida
- Utilizada para dados que não podem ser altarados'''

#Lista
#Definida entre colchetes [] e pode armazenar diferentes tipos de dados

frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misturados = ["python", 3.14, True]

print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1]) #indice negativo conta de tras para frente

# alterar valor 

frutas[0] = "uva"

print(frutas)

# adicionar elementos
''' append(): adiciona um item ao final
    insert(): adiciona um item em uma posição espefica'''

numeros.append(6)
print(numeros)

numeros.insert(1,1.5)
print(numeros)

# remover elementos
''' remove(): remove um item pelo valor
    pop(): remove um iem pelo indice ou o ultimo item se nenhum for passado'''

frutas.remove("banana")
print(frutas)

frutas.pop(0)
print(frutas)