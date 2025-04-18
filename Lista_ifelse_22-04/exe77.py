numero = int(input())
if (numero % 3 == 0 or numero % 5 == 0) and numero % 7 != 0:
    print('Múltiplo de 3 ou 5, mas não de 7')
else:
    print('Não atende')