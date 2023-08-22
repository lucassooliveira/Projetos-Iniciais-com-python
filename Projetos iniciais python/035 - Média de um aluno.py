n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a nota: '))
media = (n1 + n2)/2
if media < 5:
    print('Aluno reprovado!')
elif 5 <= media <= 6.9:
    print('Recuperação!')
elif media >= 7:
    print('Aluno aprovado!')
else:
    pass