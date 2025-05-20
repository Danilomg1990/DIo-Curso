nome="Danilo"
idade=34
profissao="Engenheiro"
linguagem="Python"
saldo=45.435
dados={"nome":"Danilo","idade":34}

print("Nome: %s idade: %d" % (nome, idade))
print("Nome: {} idade: {}" .format (nome, idade))
print("Nome: {1} idade: {0}" .format (idade, nome ))
print("Nome: {nome} idade: {idade}" .format (nome=nome, idade=idade))
print("Nome: {nome} idade: {idade}" .format (**dados))

print(f"Nome:{nome} idade: {idade}")
print(f"Nome:{nome} idade: {idade} saldo: {saldo:.2f}")
print(f"Nome:{nome} idade: {idade} saldo: {saldo:10.2f}")

