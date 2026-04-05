#Funções

'''Funções são blocos de codigos reutilizaveis que realizam uma tarefa
espeficica.Em vez de escrever o mesmo codigo varias vezes, criamos uma função
e apenas chamamos sempre que necessario.'''

#Exemplo do dia a dia

'''Calcular o imposto de varios produtos em uma loja.
Em vez de repetir a mesma conta varias vezes, criamos uma função
chamada calcular_imposto() e usamos quando precisar.'''

def saudacao (nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

saudacao("Ronnie")

def somar (a, b):
    return a + b

resultado = somar(10, 4)
print(f"A soma é {resultado}")

def calcular_media(n1, n2, n3):
    media = (n1+ n2+ n3) / 3
    return media

resultado_media = calcular_media(8, 9, 4)
print(f"A medía é {resultado_media}")