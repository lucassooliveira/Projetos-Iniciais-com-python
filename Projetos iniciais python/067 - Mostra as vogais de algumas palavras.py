palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
j = ''
l = ''
for p in palavras:
    g = p.upper()
    print(f'\nNa palavra {g} ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')