'''
A função type() em Python serve para descobrir o tipo de um objeto
ou variável em tempo de execução, retornando a classe à qual o objeto pertence.
Por exemplo, type(3.14) retornaria <class 'float'>, e type('Olá') retornaria <class 'str'>
Como usar a função type()
Basta passar a variável ou o objeto como argumento dentro dos parênteses da função.
Exemplos: Para um número inteiro.
'''
#Para numero injteiro (int)
numero_inteiro = 10
print(type(numero_inteiro))
#Saída: <class'int'>
#==============================================================================================
#Para numero decimal (float)
numero_decimal = 14.38
print(type(numero_decimal))
#Saída: <class 'float'>
#==============================================================================================
#Para uma string (texto)
texto = 'Python'
print(type(texto))
#Saída: <class 'string'>
#==============================================================================================
#Para uma lista
minha_lista = [1, 2, 3, ]
print(type(minha_lista))
#Saída: <class 'list'>
#===============================================================================================
'''
Por que usar type()?
Linguagem Dinamicamente Tipada:
Python é dinamicamente tipado, 
o que significa que o tipo de uma variável pode mudar 
durante a execução do programa.

A função type() é útil para confirmar o 
tipo de um objeto no momento da execução.

Entendimento do Código:
Permite entender o tipo de dado com o qual se está trabalhando, 
o que é importante para a lógica e para a resolução de problemas.
 
Programação Orientada a Objetos:
Em um ambiente de programação orientada a objetos, 
o tipo de uma variável é a classe da qual ela é uma 
instância. type() retorna essa classe. 
'''
#================================================================================================
#Exemplo prático
#você encontrou 4 suspeitos no seu programa:
suspeito1 = 25
suspeito2 = 'Hello World'
suspeito3 = 14.38
suspeito4 = True

#Usando type() para interrogar cada um:
print(type(suspeito1))
print(type(suspeito2))
print(type(suspeito3))
print(type(suspeito4))
#================================================================================================
#Exemplo usado em jogos
espada = 50
bau = 'poção'
critico = 25.5
vencer = True
bag = [1, 2, 3, ]

#usando type()
print(type(espada))
print(type(bau))
print(type(critico))
print(type(vencer))
print(type(bag))
