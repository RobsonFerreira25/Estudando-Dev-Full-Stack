class tinta: # criando a classe tinta
    def __init__(self, cor, qtd, base, marca): # método construtor
        self.cor = cor
        self.qtd = qtd
        self.base = base
        self.marca = marca
        
def main(): # função principal
    tinta1 = tinta("Ral 9010", 18, "Água", "Coral")
    print(f"cor: {tinta1.cor}")
    print(f"Quantidade: {tinta1.qtd} Litros")
    print(f"Base: {tinta1.base}")
    print(f"Marca: {tinta1.marca}")
    
if __name__ == "__main__": # ponto de entrada
    main()
