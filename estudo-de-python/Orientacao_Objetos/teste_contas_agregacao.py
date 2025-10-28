from contas import conta
from clientes import cliente

# Criando instâncias de clientes
cliente1 = cliente("Robson Ferreira", "123.456.789-00", "Rua A, 123")
cliente2 = cliente("Ana Paula Ferreira", "987.654.321-00", "Rua B, 456")
cliente3 = cliente("Davyna Ferreira", "456.789.123-00", "Rua C, 789")
cliente4 = cliente("Monica Ferreira", "321.654.987-00", "Rua D, 101")

# Criando uma conta com múltiplos clientes (agregação)
conta1 = conta([cliente1, cliente2, cliente3], "123.456.789-00", "0001", 5000.00)


# Testando operações na conta
conta1.gerarsaldo()
conta1.depositar(1500.00)
conta1.gerarsaldo()
if conta1.sacar(2000.00):
    print("Saque realizado com sucesso.")
conta1.gerarsaldo()




