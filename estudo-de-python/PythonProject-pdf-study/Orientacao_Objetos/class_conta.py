class conta:
    def __init__(self, titular, cpf, numero_conta, saldo):
        self.titular = titular
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
    
def main():
    conta1 = conta("Robson Ferreira", "123.456.789-00", "0001", 5000.00)
    print(f"Titular: {conta1.titular}")
    print(f"CPF: {conta1.cpf}")
    print(f"Número da conta: {conta1.numero_conta}")
    print(f"Saldo: R$ {conta1.saldo:.2f}")
        
if __name__ == "__main__":
    main()
