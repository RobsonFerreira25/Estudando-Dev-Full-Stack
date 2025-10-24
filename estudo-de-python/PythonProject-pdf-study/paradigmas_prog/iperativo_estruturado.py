#Codigo de paradigma iperativo estruturado em Python.

def contar_pares(lista): #Função que conta quantos números pares existem em uma lista
    contador = 0 #Inicializa o contador de números pares
    for numero in lista: #Percorre cada número na lista
        if numero % 2 == 0: #Verifica se o número é par
            contador += 1 #Incrementa o contador se o número for par
    return contador #Retorna o total de números pares encontrados

numeros = [10, 45, 58, 78, 55, 72, 91, 84] #Lista de números para teste
print("Quantidade de números pares na lista:", contar_pares(numeros)) #Chama a função e imprime o resultado


def conta_palavras(frase):
    palavras = frase.split() #Divide a frase em palavras usando espaço como separador
    return len(palavras) #Retorna o número de palavras na lista

frase_teste = "O paradigma estruturado é uma abordagem de programação que enfatiza a estrutura lógica do código."
print("Número de palavras na frase:", conta_palavras(frase_teste)) #Chama a função e imprime o resultado

