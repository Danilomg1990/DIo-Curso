from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

# Cliente e Conta com propriedades
class Cliente(ABC):
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido. @@@")
            return False

        if valor > self._saldo:
            print("\n@@@ Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        saques_realizados = len([
            t for t in self._historico.transacoes if t['tipo'] == 'Saque']
        )

        if saques_realizados >= self._limite_saques:
            print("\n@@@ Limite de saques diários atingido. @@@")
            return False

        if valor > self._limite:
            print("\n@@@ Valor excede o limite permitido por saque. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
Agência:	{self.agencia}
C/C:		{self.numero}
Titular:	{self.cliente.nome}
"""


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# Funções do sistema

def menu():
    print("""
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Cliente
[5] Criar Conta
[6] Listar Contas
[0] Sair
""")
    return input("Escolha uma opção: ")

def filtrar_clientes(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    if cliente.contas:
        return cliente.contas[0]
    print("@@@ Cliente não possui contas. @@@")
    return None

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("@@@ Cliente não encontrado. @@@")
        return
    valor = float(input("Informe o valor do depósito: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("@@@ Cliente não encontrado. @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    conta = recuperar_conta_cliente(cliente)
    if conta:
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)

def exibir_extrato(contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, contas)
    if not cliente:
        print("@@@ Cliente não encontrado. @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print("\n========= EXTRATO =========")
    transacoes = conta.historico.transacoes
    if not transacoes:
        print("Não foram realizadas transações.")
    else:
        for t in transacoes:
            print(f"{t['tipo']}: R$ {t['valor']:.2f} em {t['data']}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("===========================")

def criar_cliente(clientes):
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado. Crie o cliente primeiro. @@@")
        return
    conta = ContaCorrente.nova_conta(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(textwrap.dedent(str(conta)))

# Execução principal
def main():
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)
        elif opcao == "2":
            sacar(clientes)
        elif opcao == "3":
            exibir_extrato(clientes)
        elif opcao == "4":
            criar_cliente(clientes)
        elif opcao == "5":
            criar_conta(numero_conta, clientes, contas)
            numero_conta += 1
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("\n@@@ Opção inválida. Tente novamente. @@@")

if __name__ == "__main__":
    main()