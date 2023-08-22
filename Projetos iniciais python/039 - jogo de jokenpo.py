from random import choice
print('Bem vindo ao jogo de jokenpô!!!')
print('''#Escolha entre as opções:
#PEDRA
#PAPEL
#TESOURA''')
opc = str(input('Digite sua opção: ')).upper()
epc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if epc == 'PEDRA' and opc == 'PEDRA':
    print('Você e eu escolhemos pedra, deu empate!')
elif epc == 'PEDRA' and opc == 'PAPEL':
    print('Puts, eu escolhi pedra e Você escolheu papel, você venceu!')
elif epc == 'PEDRA' and opc == 'TESOURA':
    print('HAHA escolhi pedra e voce tesoura, venciii!!')
elif epc == 'PAPEL' and opc == 'PAPEL':
    print('Puts, eu escolhi papel e Você escolheu papel, deu empate de novo ;-;!')
elif epc == 'PAPEL' and opc == 'TESOURA':
    print('Escolhi papel, Não acredito que você venceu essa o,o'' ')
elif epc == 'PAPEL' and opc == 'PEDRA':
    print('Favela venceu! eu escolhi papel e Você escolheu pedra HAHA!')
elif epc == 'TESOURA' and opc == 'TESOURA':
    print('Namoral, mais um empate e eu quito tesoura e tesoura ...')
elif epc == 'TESOURA' and opc == 'PAPEL':
    print('That is it, ganhamoooooo, chupa!!Escolhi tesoura e você papel. ')
elif epc == 'TESOURA' and opc == 'PEDRA':
    print('Não existe vitória e derrota, é coisa da sua cabeça escolhi tesoura e voce pedra ;-;')
else:
    print('Opa, digitou algo errado, tente novamente!')