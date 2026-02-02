# Inserção em lista contígua com conta própria
def inserel(k, l, n):
    l.append(k)
    l[n] = k
    n = n + 1

nomes = ['Ana', 'Pedro', 'Maria', 'Carlos', 'Fernanda']
nomes.append('Fernando')
print(nomes)

inserel('Fernando', nomes, len(nomes))
