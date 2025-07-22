while True:
    nome = input("Nome: ")
    try:
        idade = int(input("idade: "))
    except ValueError:
        print("idade inválida")
        continue
    sexo = input("Sexo: ")
    cpf = int(input("CPF: "))
    endereco = input("endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
