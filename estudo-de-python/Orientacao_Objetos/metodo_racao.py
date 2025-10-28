class racao: # classe racao
    def __init__(self, sabor, peso, marca, tipo, qualidade): # método construtor
        self.sabor = sabor
        self.peso = peso
        self.marca = marca
        self.tipo = tipo
        self.qualidade = qualidade


    def alimentar(self, quantidade): # método para alimentar os pets
        if quantidade > self.peso:  # verifica se há ração suficiente
            print("Qantidade insuficiente de ração para alimentar os pets.")
        if quantidade <= self.peso: # se houver ração suficiente
            self.peso -= quantidade
            print(f"Os pets foram alimentados com {quantidade } Kg de ração.")
            
            
    def verificar_estoque(self, sacos_racao): # método para verificar o estoque de ração
        estoque_total = self.peso + (sacos_racao * self.peso) # calcula o estoque total
        print(f"Estoque total de ração: {estoque_total} Kg") # exibe o estoque total
        if estoque_total < 10: # verifica se o estoque está baixo
            print("Estoque baixo! Recomendado comprar mais ração.")
            
    
    def compra_racao(self, sacos, peso_saco): # método para comprar ração
       quantidade_comparada = sacos * peso_saco
       self.peso += quantidade_comparada
       print(f"Compra de {quantidade_comparada} Kg de ração realizada com sucesso.")
       
def main():
    racao1 = racao("Frango", 15, "Goldem", "Cães", "Premium") # criando o objeto racao1
    racao1.alimentar(20) # alimentando os pets com 5 Kg de ração
    print(f"Ração restante: {racao1.peso} Kg")
    
    racao1.verificar_estoque(2) # verifica o estoque com 2 sacos adicionais
    
    racao1.compra_racao(3, 10) # compra 3 sacos de 10 Kg cada
    print(f"Ração após compra: {racao1.peso} Kg")
    
if __name__ == "__main__": # ponto de entrada
    main()
          