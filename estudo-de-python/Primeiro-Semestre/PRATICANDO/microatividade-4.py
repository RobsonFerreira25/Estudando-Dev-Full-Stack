#Estrutura de repetição FOR
#Vamos imprimir cada letra de uma palavra e depois os numeros de 1 a 10

palavra = 'Peixe'

print('Letras da palavra:')
for letra in palavra: #Para cada letra na string 'palavra'
    print(f'Caractere: {letra}')

print('\nNumeros de 1 a 10:')
#range de 0 a 11 gera uma sequência de 1 a 10.
for numero in range(1,11): #Determina a lista de numeros a ser impressa
    print(f'Número: {str(numero)}') #str converte o numero para texto
else:

    animal = ['P', 'E', 'I', 'X', 'E']
    for indice, animal in enumerate(animal): #Use o loop FOR com enumerate(): A função enumerate() gera pares de (indice, valor) para cada elemento da lista.
        print(f'{indice}: {animal}:') #f-string formata a saida , indice e uma varialvel colocada junto com a variavel letra separada por dois pontos e espaço e assim e criada uma estrutura numero e letra em cada linha.
    
