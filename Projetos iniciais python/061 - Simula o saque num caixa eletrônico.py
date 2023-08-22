def menu():
    print('='*20)
    print('BANCO DO LUCAS')
    print('='*20)


menu()
ceda = cedb = cedc = 0
while True:
    val = int(input('Digite o valor que você quer sacar: R$ '))
    if val % 50 != 0:
        ced50 = val // 50
        ceda = val % 50
        print(f'Total de {ced50} cédulas de R$ 50')
    if ceda % 20 != 0:
        ced20 = ceda // 20
        cedb = ceda % 20
        print(f'Total de {ced20} cédulas de R$ 20')
    if cedb % 10 != 0:
        ced10 = cedb // 10
        cedc = cedb % 10
        print(f'Total de {ced10} cédulas de R$ 10')
    if cedc != 0:
        ced1 = cedc // 1
        print(f'Total de {ced1} cédulas de R$ 1')
    break
print('Volte sempre ao BANCO DO LUCAS! Tenha um bom dia!')