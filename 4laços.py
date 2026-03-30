# LAÇOS DE REPETIÇÃO

'''Os laços de repetição são usados para executar um bloco de codigo varias vezes
ate que uma condição seja atingida. '''

#Python tem dois tipos principais de laços:

#for -> Quando sabemos quantas vezes queremos repetir algo.
#while -> Quando queremos repetir algo ate que uma condição se torne falsa.


#Estrutura for

'''for VARIAVEL in SEQUENCIA():
    CODIGO A SER REPETIDO'''

'''for '''

for numero in range(1,11):
    print(numero)

compras = ["arroz", "feijão", "batata", "frango"]

for itens in compras:
    print(f"Comprar: {itens}")

palavra = "Ronnie"

for letra in palavra:
    print(letra)

'''while CONDIÇÃO:
    CODIGO A SER REPETIDO'''

#Cuidado com loops infinitos!!   Para encerrar o looping no Windows: Ctrl + C

contador = 10

while contador > 0:
    print(contador)
    contador -= 1  #Diminui 1 do contador a cada repetição 


senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso liberado")