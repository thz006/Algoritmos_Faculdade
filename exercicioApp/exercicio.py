import os

listaDeListas = []

while True:
    userLista = []

    try:
        nome = input("Digite o seu nome: ").title()
    except:
        print("Erro no nome!")
        continue

    while True:
        idade = input('Idade: ')
        if idade.isdigit() and 0 < int(idade) < 120:
            break
        else:
            print('Digite uma idade válida!')

    while True:
        sexo = input("Digite o seu sexo (F ou M): ").lower()
        if sexo in ["f", "m"]:
            break
        else:
            print("Digite apenas F ou M.")

    while True:
        cpf = input("CPF (11 dígitos): ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("CPF inválido")

    try:
        endereco = input("Digite o seu endereço: ").title()
    except:
        print("Erro no endereço!")
        continue

    try:
        cidade = input("Digite a sua cidade: ").title()
    except:
        print("Erro na cidade!")
        continue

    try:
        estado = input("Digite o seu estado (sigla): ").upper()
    except:
        print("Erro no estado!")
        continue

    userLista.extend([nome, idade, sexo, cpf, endereco, cidade, estado])
    listaDeListas.append(userLista)

    with open("exercicioApp/arquivo.txt", "w") as arquivo:
        for pessoa in listaDeListas:
            arquivo.write(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Sexo:{pessoa[2].upper()}, Endereço: {pessoa[4]}, Cidade: {pessoa[5]}, Estado: {pessoa[6]}\n")
            arquivo.write("-----------------------------------------------------------------------------------------------------\n")

    while True:
        try:
            acao = int(input("1. Cadastrar nova pessoa\n2. Consultar dados\n3. Sair\nEscolha: "))
            break
        except ValueError:
            print("Digite 1, 2 ou 3.")

    if acao == 1:
        continue

    elif acao == 2:
        try:
            with open("exercicioApp/arquivo.txt", "r") as arquivo:
                linhas = arquivo.readlines()
                pessoas = [i for i in range(0, len(linhas), 2)]

                for idx in range(len(pessoas)):
                    print(f"{idx + 1}. {linhas[pessoas[idx]].strip()}")

                escolha = int(input("Digite o número da pessoa que deseja consultar: "))
                if 1 <= escolha <= len(pessoas):
                    print(linhas[pessoas[escolha - 1]])
                else:
                    print("Número inválido.")
        except FileNotFoundError:
            print("Arquivo ainda não foi criado.")
        except Exception as e:
            print(f"Erro: {e}")

    elif acao == 3:
        print("Programa encerrado. Dados salvos no arquivo 'arquivo.txt'.")
        break

    else:
        print("Opção inválida.")
