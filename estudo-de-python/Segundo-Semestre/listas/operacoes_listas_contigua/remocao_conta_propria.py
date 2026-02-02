# Remocao em lista contígua com conta própria
def removeL(k, l, n):
    i = 0
    while i < n:
        if l[i] == k:
            i = n + 1
        else:
            i = i + 1
    if i == n:
        return -1
    else:
        i = i - 1
        while i < n - 1:
            l[i] = l[i + 1]
            i = i + 1
        n = n - 1
        return n

nomes = ['Ana', 'Pedro', 'Maria', 'Carlos', 'Fernanda']
nome_removido = 'Maria'
removeL(nome_removido, nomes, len(nomes))
print(nomes)