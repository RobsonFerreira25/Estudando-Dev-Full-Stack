# codigo iperativo orientado a objeto em Python.

class conta: #Definição da classe conta
    def __init__(self, titular, cpf, numero_conta, saldo): #Construtor da classe conta
        self.titular = titular
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
    
def main(): #Função principal para testar a classe conta
    conta1 = conta("Robson Ferreira", "123.456.789-00", "0001", 5000.00)
    print(f"Titular: {conta1.titular}")
    print(f"CPF: {conta1.cpf}")
    print(f"Número da conta: {conta1.numero_conta}")
    print(f"Saldo: R$ {conta1.saldo:.2f}")
        
if __name__ == "__main__": #Ponto de entrada do programa
    main()


class produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        
    def desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto
    
def main():
    produto1 = produto('notebook', 4500.00, 5)
    print(f"Produto: {produto1.nome}")
    print(f"Preço original: R$ {produto1.preco:.2f}")
    preco_com_desconto = produto1.desconto(10) # Aplicando 10% de desconto
    print(f"Preço com desconto: R$ {preco_com_desconto:.2f}")
    
if __name__ == "__main__":
    main()
