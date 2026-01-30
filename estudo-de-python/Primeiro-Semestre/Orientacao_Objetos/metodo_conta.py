class conta:
    def __init__(self, titular, cpf, numero_conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso.")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            
def main():
    conta1 = conta("Robson Ferreira", "123.456.789-00", "0001", 5000.00)
    conta1.depositar(1500.00)
    print(f"Saldo atual: R$ {conta1.saldo:.2f}")
    
    conta1.sacar(2000.00)
    print(f"Saldo atual: R$ {conta1.saldo:.2f}")
    
if __name__ == "__main__":
    main()