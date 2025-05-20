from os import system as limp
limp("cls")

conta_normal=False
conta_universtaria=True

saldo=2000
saque=1500
cheque_especial=450

if conta_normal:
    if saldo>=saque:
        print("Saque realizado com sucesso!")
    elif saque<=(saldo+ cheque_especial):
        print("Saque realizado com sucesso com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque, saldo insulficiente!")
elif conta_universtaria:
    if saldo>=saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insulficiente!")
else: 
    print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente do banco!")