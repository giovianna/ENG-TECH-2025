import os

saldo = 1000

while True:
    print("=====Caixa Eletrônico====")
    print("1. Consultar Saldo")
    print("2. Sacar dinheiro")
    print("3. Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")
    elif opcao == 2:
        saque = float(input("Digite o valor do saque: R$ "))  
        if saque > saldo:
            print("Saldo insuficiente!")
        elif saque <= 0:
            print("Valor inválido")
        else:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {saldo:.2f}")
    elif opcao == 3:
        print("Saindo... Obrigado por utilizar nosso Caixa Eletrônico!")
        break
    else:
        print("Opção inválida! Escolha uma opção do 1 ao 3.")

    input("\nPressione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")    





