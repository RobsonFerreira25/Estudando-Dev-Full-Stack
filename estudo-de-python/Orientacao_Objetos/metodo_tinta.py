class tinta: # criando a classe tinta
    def __init__(self, cor, qtd, base, marca): # método construtor
        self.cor = cor
        self.qtd = qtd
        self.base = base
        self.marca = marca
        
    def definir_cor(self, nova_cor): # método para definir nova cor
        self.cor = nova_cor
        print(f"A cor da tinta foi alterada para {self.cor}")
        
    def definir_qtd(self, nova_qtd): # método para definir nova quantidade
        self.qtd = nova_qtd
        print(f"A quantidade de tinta foi alterada para {self.qtd} Litros.")
        
    def definir_base(self, nova_base): # método para definir nova base
        self.base = nova_base
        print(f"A base de tinta foi alterada para {self.base}")
        
    def definir_marca(self, nova_marca): # método para definir nova marca
        self.marca = nova_marca
        print(f"A marca da tinta foi alterada para {self.marca}")
        
    def pintar(self, area): # método para pintar uma área
        tinta_necessaria = area / 10  # considerando que 1 litro pinta 10 m²
        if tinta_necessaria > self.qtd:
            print("Quantidade de tinta insuficiente para pintar a área desejada.")
        else:
            self.qtd -= tinta_necessaria
            print(f"Área de {area} m² pintada com sucesso. Tinta restante: {self.qtd} Litros.")
            
    def medir_parede(self, largura, altura): # método para medir a parede
        area = largura * altura
        print(f"A área da parede é {area} m².")
        return area
    
    def selecionar_cor(self, cor_escolhida): # método para selecionar cor
        cores_disponiveis = ["Branco", "Preto", "Azul", "Vermelho", "Verde", "Amarelo"]
        input_cor = cor_escolhida
        if input_cor in cores_disponiveis:
            self.cor = input_cor
            print(f"A cor {self.cor} foi selecionada com sucesso.")
            
def main(): # função principal
    tinta1 = tinta("Ral 9010", 18, "Água", "Coral")
    tinta1.definir_cor("Azul")
    tinta1.definir_qtd(20)
    tinta1.definir_base("Água Acrílica")
    tinta1.definir_marca("Suvinil")
    
    area_parede = tinta1.medir_parede(5, 3)  # Medindo uma parede de 5m x 3m
    tinta1.pintar(area_parede)  # Pintando a parede medida
    
    tinta1.selecionar_cor("Verde")  # Selecionando a cor verde
    
if __name__ == "__main__": # ponto de entrada
    main()
            
    