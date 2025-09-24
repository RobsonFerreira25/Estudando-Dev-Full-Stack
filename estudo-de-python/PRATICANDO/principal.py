from imc import calcula_imc
from imc import classifica_imc

print('Inicio do programa')
indice = calcula_imc(peso=100, altura=1.78)
print('IMC:', indice)
classifica_imc = classifica_imc(indice)
print(classifica_imc)
print('Fim do programa')

