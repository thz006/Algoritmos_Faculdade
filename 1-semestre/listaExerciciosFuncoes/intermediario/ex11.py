def calculadora(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else 'Divisão por zero'
    else:
        return 'Operação inválida' 