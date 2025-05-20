from os import system as limp

def menu():
    tela_inicial = f"""
        #################    Bem-Vindo ao Banco   ##################
        #                            |       ##############        #
        #  Selecione um opção:       |       ##############        #
        #                            |       ####      ####        #
        #   [1] Depositar            |       ###   ##   ###        #
        #   [2] Sacar                |       #######   ####        #
        #   [3] Extrato              |       ######  ######        #
        #   [4] Sair                 |       ##############        #
        #                            |       ######  ######        #
        ############################################################
    """
    print(tela_inicial)

while True:
    limp('cls')  # ou use: limp('clear') se estiver no Linux/Mac

    menu()  # Corrigido: chamada da função

    try:
        opcao = int(input("Selecione uma opção acima: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        input("Pressione Enter para continuar...")
        continue

    if opcao == 1:
        print("Você escolheu: Depositar")
    elif opcao == 2:
        print("Você escolheu: Sacar")
    elif opcao == 3:
        print("Você escolheu: Extrato")
    elif opcao == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")

    input("Pressione Enter para continuar...")

    