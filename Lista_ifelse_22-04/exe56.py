numero = int(input())
if numero > 0 and numero % 3 == 0 and numero % 5 != 0:
    print('Positivo, múltiplo de 3 e não de 5')
else:
    print('Não atende')