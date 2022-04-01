a = input('Você gostaria de calcular? s/n -> ')

if a == 's':
    num = input('Digite a conta: ')
    print(eval(num))
elif a == 'n':
    print('Boboca')
else:
    print('OTARO')
