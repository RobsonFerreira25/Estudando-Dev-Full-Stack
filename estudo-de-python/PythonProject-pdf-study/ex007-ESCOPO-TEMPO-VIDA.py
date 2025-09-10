#Ecopo global e tempo de vida na linguagem python
'''
# é a região de um programa onde um nome
(como uma variável) é diretamente acessível.

Global:
Variáveis definidas fora de qualquer função,
no corpo principal do script. Podem ser
acessadas em qualquer lugar do programa.

Escopo Global vs Escopo Local:
o escopo local refere-se a variáveis definidas
numa função, acessíveis apenas dentro dessa função
e que desaparecem quando a função termina,
enquanto o escopo global se aplica a variáveis definidas
fora de qualquer função, que podem ser
acessadas de qualquer lugar do programa.

Escopo Local
Definição: Variáveis declaradas numa função.
Acessibilidade: Só podem ser acessadas dentro da função onde foram criadas.
Ciclo de Vida: As variáveis locais são criadas quando a
função é chamada e destruídas quando a função termina.
'''
#=============================================================================
def minha_funcao():
    variavel_local = 10 #Esta é uma variavel local
    print(variavel_local)

'''    
minah_funcao()
    print(variavel_local) #isso geraria um erro pois a variavel local
nao existe fora da função
'''
#==============================================================================
'''
Escopo Global
Definição:
Variáveis declaradas fora de qualquer função, no nível principal do script.
Acessibilidade:
Podem ser acessadas de qualquer lugar do código, inclusive dentro de funções.
Modificação dentro de função:
Se você precisar modificar uma variável global a partir de uma função, 
deve usar a palavra-chave global.
'''
#===============================================================================
variavel_global = 'sou global'
def minha_funcao_global():
    global variavel_global #Isso indica que queremos usar a variavel global
    variavel_global = 'Modificada Globalmente'
    print(variavel_global)

minha_funcao_global()
print(variavel_global) #A variavel tera o valor modificado
#================================================================================
'''
Importância do Uso Consciente
Embora as variáveis globais sejam úteis para compartilhar dados, 
o seu uso excessivo pode tornar o código mais difícil de ler, 
manter e pode causar problemas de rastreamento de erros, 
dificultando o entendimento de quem modificou a variável. 
'''
#================================================================================
#Exemplo pratico
inimigos_globais = 10 #Variavel global (todo o codigo ve)
def dungeon():
    inimigos_locais = 5 #Variavel local (so existe aqui)
    print('dentro da dungeon', inimigos_locais) #Funciona!
    print('fora da dungeon', inimigos_globais) #Tambem Funciona
dungeon()
print('Fora da dungeon', inimigos_globais) #funciona
print('tentando ver inimigos locais fora') #erro não existe aqui
#================================================================================
#tempo de vida
'''
Variaveis locais nascem quando uma função e chamada e morrem
quando ela termina.
Variaveis Globais: Vivem ate o programa acabar
'''
#================================================================================
#Exemplo com tempo de vida:
def pocao():
    cura = 50
    print('cura dentro:', cura)
pocao()
#print(cura) #erro! 'cura' já morreu após a função terminar.
#================================================================================
#Cuidado com Variaveis Globais (Armadilha Comum)
#Modificar variaveis globais dentro de funções exige o comando "global:"
ouro = 100

def vender_iten():
    global ouro #Opa posso modificar a variavel global?
    ouro += 50
vender_iten()
print(ouro) #150
#================================================================================
#Sem Global
ouro = 100

def vender_iten():
    ouro = 50 #isso cria uma nova variavel local
    print('dentro', ouro) #50
vender_iten()
print('fora', ouro) #100 (global não foi alterada)
#================================================================================
'''
1. Use variaveis locais sempre que possivel (evita conflitos)
2. Evite modificar globais dentro de funções (é propenso a bugs)
3. lembre-se: escopo de função ≠ escopo de condicionais loop
'''
#================================================================================
if True:
    x = 10 #isso e global em Python cuidado
print(x) #10
#================================================================================
#Desafio Mental
#O que esse codigo imprime
vida = 100

def curar():
    vida = 150
    print('durante a cura', vida)
curar()
print('depois da cura', vida)
#================================================================================
