from os import system as limp
limp('cls')

maior_idade=18
idade_especial=17

idade=int(input("Informe sau idade: "))

if idade>=maior_idade:
    print("Maior de idade, pode tirar CNH.")

if idade<maior_idade:
    print("Ainda não pode tirar a CNH.")

if idade>=maior_idade:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar a CNH.")

if idade>=maior_idade:
    print("Maior de idade, pode tirar CNH.")

elif idade==idade_especial:
    print("Pode fazer aulas teoricas mas não pode fazer aulas praticas.")
else:
    print("Ainda não pode tirar a CNH.")
