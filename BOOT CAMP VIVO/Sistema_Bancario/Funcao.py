def sacar_tela(*,saldo,extrato,limite,numero_saque,limite_saque):
    
    try:
        print("########## SAQUE ##########\n")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
        valor = float(input("Digite o valor que deseja sacar: R$ "))
        excedeu_saldo=valor>saldo
        excedeu_limite=valor>limite
        excedeu_saques=numero_saque>limite_saque

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Valor excedeu o limite.")
        elif excedeu_saques:
            print("Valor excedeu o numero maximo de saque.")
        else:
            saldo -= valor
            extrato.append(f"Saque: \t\t\t- R${valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")
    input("Pressione Enter para continuar...")
    return saldo,extrato

def depositar_tela(saldo,extrato,/):
    try:
        print("########## DEPOSITO ##########\n")
        valor = float(input("Digite o valor que deseja depositar: R$ "))
        if valor <= 0:
            print("Valor inválido. Digite um valor positivo.")
        else:
            saldo += valor
            extrato.append(f"Depósito: \t\t+ R${valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")
    input("Pressione Enter para continuar...")
    return   saldo,extrato

def extrato_tela(saldo,/,*,extrato):
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        print("########## EXTRATO ###############\n")
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual:\t\tR$ {saldo:.2f}")
    print("##################################")
    input("Pressione Enter para continuar...")
    return saldo,extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Usuário já existente!")
        input("Pressione Enter para continuar...")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    })

    print("Usuário criado com sucesso!")
    input("Pressione Enter para continuar...")
    return usuarios

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)

    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado. Crie o usuário primeiro.")

    input("Pressione Enter para continuar...")
    return contas

def listar_contas(contas):
    print("########## LISTAR CONTAS ##########\n")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print("=" * 40)
            print(f"Agência:\t{conta['agencia']}")
            print(f"Número:\t\t{conta['numero_conta']}")
            print(f"Titular:\t{conta['usuario']['nome']}")
    input("\nPressione Enter para continuar...")