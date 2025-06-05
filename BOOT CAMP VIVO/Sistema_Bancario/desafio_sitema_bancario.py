from os import system as limp
limp('cls')
import Funcao as oper
import Menu as men


def main():
    limite_saque=0
    agencia="0001"

    saldo = 0
    limite=500
    numero_saque=0
    extrato = []
    usuario =[]
    contas=[]

    while True:
        limp('cls')
        print(men.menu_tela())

        try:
            opcao = int(input("Selecione uma opção acima: "))
            print()
        except ValueError:
            print("Por favor, digite um número válido.")
            input("Pressione Enter para continuar...")
            continue

        if opcao == 1:#Deposit0
           saldo,extrato= oper.depositar_tela(saldo,extrato)
           continue
        elif opcao == 2:#Sacar
            saldo,extrato=oper.sacar_tela(
                saldo=saldo,
                extrato=extrato,
                limite = limite,
                numero_saque=numero_saque,
                limite_saque=limite_saque,
            )
            continue
        elif opcao == 3:#Extrato
           saldo,extrato=oper.extrato_tela(saldo,extrato=extrato)
           continue
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
        return
main()