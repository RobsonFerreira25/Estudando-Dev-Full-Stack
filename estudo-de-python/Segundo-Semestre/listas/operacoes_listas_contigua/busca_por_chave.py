def buscalista(k, l, n): # k = chave, l = lista, n = tamanho da lista
    i = 0   # i = indice
    indicel = -1 # indicel = indice do elemento buscado
    while i < n: # percorre a lista
        if l[i] == k: # verifica se o elemento atual é igual a chave
            indicel = i # se for, armazena o indice
            i = n + 1 # e sai do loop
        i = i + 1 # incrementa o indice
    return indicel

nomes = ['Ana', 'Pedro', 'Maria', 'Carlos', 'Fernanda']
nome_buscado = 'Fernanda'

print(buscalista(nome_buscado, nomes, len(nomes)))
