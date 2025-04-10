salario = float(input("salario: "))

if salario < 500:
    reajuste = salario + ( salario * 0.15)
    print(f"salario com reajuste: {reajuste}")
elif salario <= 1000:
    reajuste = salario + ( salario * 0.10)
    print(f"salario com reajuste: {reajuste}")
elif salario > 1000:
    reajuste = salario + ( salario * 0.05)
    print(f"salario com reajuste: {reajuste}")