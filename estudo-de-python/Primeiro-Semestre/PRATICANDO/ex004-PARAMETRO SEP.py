#Parametro SEP
#Sintaxe
#print(valor1, valor2, valor3, sep= separador)
#Exemplaos praticos
#1. Padrao espaço
print('Python', 'é', 'íncrivel') #saida: Python é íncrivel
#-------------------------------------------------------------------------------------------
#2. Personalizado com virgula e traço
print('Python', 'é', 'íncrivel', sep= ',') #Saida: Python, é, íncrivel
print('Python', 'é', 'íncrivel', sep= '-') #Saida: Python-é-íncrivel
#-------------------------------------------------------------------------------------------
#3. Criativo (usando emojis ou simbolos)
print('café', 'pão', 'queijo', sep='&') #Saida: café&pão&queijo
#-------------------------------------------------------------------------------------------
#Para dominar o SEP, basta lembar:
#1. A funcão SEP controla o separador de itens no print()
#2. O valor padrão e espaço (" ")
#3. Personalização: use strings como sep=(",") ou sep("\n") para quebra de linha e etc...
#-------------------------------------------------------------------------------------------
#Exemplo Utíl
#imprima uma lista de compras em uma linha só, separada por traços
itens = ['maçã', 'leite', 'ovos']
print(*itens, sep='-')
'''
o * acompanhado da variavel itens serve para desempacotar a lisa de itens separados
Desempacotamento de lista com *
Se você tiver uma lista e quiser passar seus elementos
como argumentos individuais para uma função, pode usar o asterisco *: 
'''
def minha_funcao(a, b, c):
  print(a, b, c)

minha_lista = [1, 2, 3]
minha_funcao(*minha_lista)  # Desempacota a lista e chama a função como minha_funcao(1, 2, 3)
# Saída: 1 2 3
