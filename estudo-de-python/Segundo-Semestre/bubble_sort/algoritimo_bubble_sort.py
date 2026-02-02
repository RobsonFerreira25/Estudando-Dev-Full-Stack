# Algoritimo Bubble Sort

from random import shuffle
from os import system

system('cls')

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
shuffle(vetor)
print(vetor)

for i in range(len(vetor)):
    for j in range(len(vetor) - 1): # -1 para não comparar o último elemento com ele mesmo
        if vetor[j] > vetor[j + 1]: # se o elemento atual for maior que o próximo
            vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j] # troca os elementos
            print(vetor)
