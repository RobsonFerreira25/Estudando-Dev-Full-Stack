'''
Os operadores básicos em Python incluem os aritméticos
(+, -, *, /, //, %, **), que realizam cálculos; os de comparação
(==, !=, >, <, >=, <=), que comparam valores; os lógicos (and, or, not),
que combinam condições booleanas; os de atribuição (=, +=, -=, etc.), que
atribuem valores; e os de identidade (is, is not), que verificam
se dois objetos são o mesmo na memória.

Operadores Aritméticos
Realizam operações matemáticas:
+: Adição
-: Subtração
*: Multiplicação
/: Divisão (retorna um número de ponto flutuante)
//: Divisão inteira (arredonda para baixo)
%: Módulo (resto da divisão)
**: Exponenciação

Operadores de Comparação
Comparam dois valores, retornando True ou False:
==: Igual a
!=: Diferente de
>: Maior que
<: Menor que
>=: Maior ou igual a
<=: Menor ou igual a

Operadores Lógicos
Combinam expressões booleanas:
and: Retorna True se ambas as condições forem verdadeiras.
or: Retorna True se pelo menos uma das condições for verdadeira.
not: Inverte o valor booleano (se for True, retorna False, e vice-versa).

Operadores de Atribuição
Atribuem valores a variáveis:
=: Atribuição simples
+=, -=, *=, /=, %=, //=, **=: Realizam a operação e atribuem o resultado
 à variável (ex: x += 5 é o mesmo que x = x + 5).

Operadores de Identidade
Verificam se dois objetos se referem à mesma posição na memória:
is: Retorna True se os operandos são o mesmo objeto.
is not: Retorna True se os operandos não são o mesmo objeto.
'''
#===================================================================================
#Exemplo prático
vida_inimigo = 100
dano_espada = 25
dano_magico = dano_espada * 3 #75 de critico
vida_inimigo -= dano_magico #Vida agora é 25
print(vida_inimigo, 'Inimigo ainda vivo') #25
#===================================================================================
#Operadores de atribuição (Upgrades Rápidos)
#São atalhos para modificar variáveis:
'''
Operador| Equivalente a | Exemplo     |
+=      | x = x + y     | vida += 100 |
-=      | x = x - y     | energia -= 5|
*=      | x = x * y     | dano *= 1.5 |
'''
#===================================================================================
#Exemplpo
ouro = 100
ouro += 50 #Achou um bau agora tem 150
print(ouro, 'Opa, um bau com 50 de gold')
#===================================================================================
#Operadores Úteis (Mas Menos Óbvios)
#1. Módulo (%)
#decobre se um número e par ou ímpar:
numero = 0
if numero % 2 == 0:
    print('Esse número é Par !')
#===================================================================================
#2. Divisão inteira (//)
posicao_x = 15 // 4 #Operação
print(posicao_x, 'É a sua posição') #Resultado (// inteira ignora números decimais)
#===================================================================================
#Exponenciação (**)
#cauculo de área quadrada
area = 0
lado = 10
area  = lado ** 2
print(area, 'Essa é a área total em metros.')
#===================================================================================
#Desafio Prático
'''
#Caucule quantas poções de cura (+ 25 HP) um jogador precisa para recuperar
toda sua vida (HP_MAX = 120), sabendo que ele esta com um HP_ATUAL = 45 :
'''
#===================================================================================
POCOES = 25
HP_MAX = 120
DANO = 120 - 45
POCOES = DANO // 25 #Quantas poções INTEIRAS (pois a divisão inteira ignora decimais)
print(POCOES, 'Poções são necessárias.')