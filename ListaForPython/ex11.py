preco=float(input("digite o preço do pão: "))
for i in range(1,51):
    result = i * preco
    print(f"{i}-{result:.2f}")