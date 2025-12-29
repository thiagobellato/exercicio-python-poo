class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
            return True
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
            return True
        else:
            print("Saldo insuficiente para saque.")


conta_thiago = ContaBancaria("Thiago", 0)
conta_thiago.depositar(1000)
print(f"Saldo da conta de {conta_thiago.titular}: R${conta_thiago.saldo}")
conta_thiago.sacar(100)
print(f"Saldo da conta de {conta_thiago.titular} após saque: R${conta_thiago.saldo}")
