class racao:
    def __init__(self, sabor, peso, marca, tipo, qalidade):
        self.sabor = sabor
        self.peso = peso
        self.marca = marca
        self.tipo = tipo
        self.qualidade = qalidade
        
def main():
    racao1 = racao("Frango", 15, "Golden", "Cães", "Premium")
    print(f"Sabor: {racao1.sabor}")
    print(f"Peso: {racao1.peso} Kg")
    print(f"Marca: {racao1.marca}")
    print(f"Tipo: {racao1.tipo}")
    print(f"Qualidade: {racao1.qualidade}")
    
if __name__ == "__main__":
    main()

