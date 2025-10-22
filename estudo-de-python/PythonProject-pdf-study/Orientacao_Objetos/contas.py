class conta:
    def __init__(self, clientes, cpf, numero_conta, saldo):
        self.clientes = clientes
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
        
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
    def transferir(self, valor, conta_destino):
        if self.saldo < valor:
            return ("Saldo insuficiente para transferência.")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            return ("Transferencia realizada com sucesso.")
        
    def gerarsaldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        
    