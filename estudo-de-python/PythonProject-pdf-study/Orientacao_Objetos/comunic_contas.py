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
            
    def transferir(self, valor, conta_destino): # método para transferir dinheiro
        if valor > self.saldo:
            print("Saldo insuficiente para transferência.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso para {conta_destino.titular}.")
            
def main():
    conta1 = conta("Robson Ferreira", "123.456.789-00", "0001", 5000.00)
    conta2 = conta("Ana Paula Ferreira", "987.654.321-00", "0002", 3000.00)
    
    conta1.transferir(2000.00, conta2) # transferindo R$ 2000,00 da conta1 para a conta2
    print(f"Saldo atual de {conta1.titular}: R$ {conta1.saldo:.2f}")
    print(f"Saldo atual de {conta2.titular}: R$ {conta2.saldo:.2f}")
    
if __name__ == "__main__":
    main()

    
    