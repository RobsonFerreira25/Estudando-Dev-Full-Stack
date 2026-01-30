def hello():
    print('Olá')
    print('Mundo')

hello()

def calculo_imc(peso, altura):
    imc = peso/altura**2
    print('parâmetro peso:', peso)
    print('parâmetro altura', altura)
    print('IMC:', imc)

# Inicio do programa
print('Inicio do programa')
calculo_imc(70, 1.80)
print('Termino do programa')

def calculo_imc(peso, altura):
    imc = peso/altura**2
    print('parâmetro peso:', peso)
    print('parâmetro altura', altura)
    print('IMC:', imc)

# Inicio do programa
print('Inicio do programa')
calculo_imc(altura=1.80, peso=70)
print('Termino do programa')