pal = str(input('Digite uma frase qualquer: ')).strip().upper()
pal1 = pal.split()
junt = ''.join(pal1)
invers = ''
for c in range(len(junt) -1, -1, -1):
    invers += junt[c]
print('O inverso da frase {} digitada é {}'.format(junt, invers))
if junt == invers:
    print('Esta frase é um PALÍNDROMO!')