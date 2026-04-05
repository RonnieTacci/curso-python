#Simular um caixa eletronico

'''O usuario tem um saldo inicial de 500 reais e pode
sacar dinheiro ate zerar o saldo ou encerrar.'''

saldo = 500

while saldo > 0:
    saque= int(input("Informe o valor do saque ou digite 0 para sair. "))

    if saque == 0:
        break

    if saque > saldo:
        print("Saldo insuficiente! Saque não efetuado.")
    else:
        saldo -= saque
        print(f"Saque efetuado.Novo saldo:{saldo}")

print("Operação finalizada.")