# Inserção em lista contígua ordenada
def insereOrdenada(k, l, n):
    i = 0
    posInsercao = -1
    while i < n: # percorre a lista
        if l[i] >= k: # verifica se o elemento atual é maior ou igual a chave
            if l[i] == k: # se for, retorna -1
                return -1
            else: # se não for, armazena o indice
                posInsercao = i
                i = n + 1
        else: # se não for, incrementa o indice
            i = i + 1
    if i == n: # se o indice for igual ao tamanho da lista, armazena o indice
        posInsercao = n
l.append('')
i = n
while i > posInsercao: # percorre a lista
    l[i] = l[i - 1] # move os elementos
    i = i - 1
l[posInsercao] = k # insere o elemento
return posInsercao

numeros=[1,2,3,4,6,7,8,9,10]
insereL(12,numeros,len(numeros))
print(numeros)
insereOrdenada(5,numeros,len(numeros))
print(numeros)


    