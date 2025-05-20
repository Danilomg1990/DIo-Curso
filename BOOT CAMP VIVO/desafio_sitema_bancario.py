from os import system as limp
limp('cls')


saldo = 1000
extrato = []

def menu_tela():
    tela_inicial = f"""
        ################    Bem-Vindo ao Banco   ###################
        #                            |##############################     
        #  Selecione um opção:       |##############################
        #                            |###########      #############    
        #   [1] Depositar            |##########   ##   ############       
        #   [2] Sacar                |##############   #############     
        #   [3] Extrato              |#############  ###############     
        #   [4] Sair                 |##############################
        #                            |#############  ###############
        ############################################################
    """
    print(tela_inicial)

def sacar_tela():
    global saldo
    try:
        limp('cls')

        print("########## SAQUE ##########\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        if valor <= 0:
            print("Valor inválido. Digite um valor positivo.")
        elif valor > saldo:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            extrato.append(f"Saque: - R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")
    input("Pressione Enter para continuar...")

def depositar_tela():
    global saldo
    try:
        limp('cls')
        print("########## DEPOSITO ##########\n")
        valor = float(input("Digite o valor que deseja depositar: R$ "))
        if valor <= 0:
            print("Valor inválido. Digite um valor positivo.")
        else:
            saldo += valor
            extrato.append(f"Depósito: + R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")
    input("Pressione Enter para continuar...")

def extrato_tela():
    limp('cls')
    print("########## EXTRATO ##########")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("#############################")
    input("Pressione Enter para continuar...")

while True:
    limp('cls')
    menu_tela()

    try:
        opcao = int(input("Selecione uma opção acima: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        input("Pressione Enter para continuar...")
        continue

    if opcao == 1:
        depositar_tela()
    elif opcao == 2:
        sacar_tela()
    elif opcao == 3:
        extrato_tela()
    elif opcao == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...")