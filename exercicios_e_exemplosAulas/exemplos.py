while True:
    nome = input("nome: ")
    if len(nome) >= 3:
        break
    print("Nome precisa ter 3 ou mais caracteres.")
while True:
    try:
        idade = int(input("idade: "))
    except ValueError:
        print("Digite um número inteiro para idade.")
        continue

    if 0 <= idade <= 150:
        break
    print("Idade deve estar entre 0 e 150.")
while True:
    try:
        salario = float(input("salario: "))
    except ValueError:
        print("Digite um número válido para salário.")
        continue
    if salario > 0:
        break
    print("Salário deve ser maior que zero.")
while True:
    sexo = input("sexo (f/m/o): ").lower()
    if sexo in ('f', 'm', 'o'):
        break
    print("Sexo inválido. Apenas 'f', 'm' ou 'o'.")
while True:
    civil = input("civil (s/c/v/d): ").lower()
    if civil in ('s', 'c', 'v', 'd'):
        break
    print("Estado civil inválido. Apenas 's', 'c', 'v' ou 'd'.")
print("\nDados válidos:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Civil: {civil}")