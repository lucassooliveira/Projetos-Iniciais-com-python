peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso/(altura ** 2)
if imc < 18.5:
    print('Abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Peso ideal!')
elif 25 < imc <= 30:
    print('Sobrepeso!')
elif 30 < imc <= 40:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade mórbida!')