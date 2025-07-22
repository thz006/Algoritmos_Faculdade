num1 = int(input())
num2 = int(input())
soma = num1 + num2
if soma > 100 and soma % 10 == 0:
    print('Soma maior que 100 e múltiplo de 10')
else:
    print('Não atende')