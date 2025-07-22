clientes = []
passagens = []
avioes = []
tripulacao = []

def menu_principal():
    while True:
        print("\nPASSAGENS AÉREAS")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Passagem")
        print("3. Cadastrar Avião")
        print("4. Cadastrar Tripulação")
        print("5. Imprimir Relatórios")
        print("6. Encerrar")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                cadastrar_cliente()
            elif opcao == 2:
                cadastrar_passagem()
            elif opcao == 3:
                cadastrar_aviao()
            elif opcao == 4:
                cadastrar_tripulacao()
            elif opcao == 5:
                imprimir_relatorios()
            elif opcao == 6:
                print("Encerrando sistema...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números!")

def cadastrar_cliente():
    try:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        rg = input("RG: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        fone = input("Telefone: ")
        idade = int(input("Idade: "))

        cliente = {
            "Nome": nome,
            "Sobrenome": sobrenome,
            "RG": rg,
            "CPF": cpf,
            "Endereço": endereco,
            "Fone": fone,
            "Idade": idade
        }
        clientes.append(cliente)
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")

def cadastrar_passagem():
    try:
        origem = input("Origem: ")
        destino = input("Destino: ")
        duracao = input("Duração do Voo em horas: ")
        valor = float(input("Valor da Passagem: "))
        desconto = valor * 0.05
        valor_final = valor - desconto

        passagem = {
            "Origem": origem,
            "Destino": destino,
            "Duração": duracao,
            "Valor Original": valor,
            "Desconto": desconto,
            "Valor Final": valor_final
        }
        passagens.append(passagem)
        print("Passagem cadastrada com sucesso!")
    except ValueError:
        print("Valor inválido. Digite um número para o valor da passagem.")

def cadastrar_aviao():
    try:
        modelo = input("Modelo do avião: ")
        ano = int(input("Ano: "))
        horas_voo = float(input("Horas de voo: "))
        cor = input("Cor: ")
        qtd_passageiros = int(input("Quantidade de passageiros: "))

        aviao = {
            "Modelo": modelo,
            "Ano": ano,
            "Horas de Voo": horas_voo,
            "Cor": cor,
            "Qtd Passageiros": qtd_passageiros
        }
        avioes.append(aviao)
        print("Avião cadastrado com sucesso!")
    except ValueError:
        print("Erro nos dados numéricos. Verifique e tente novamente.")

def cadastrar_tripulacao():
    try:
        nome = input("Nome: ")
        cargo = input("Descrição do Cargo: ")
        idade = int(input("Idade: "))
        data_admissao = input("Data de Admissão (dd/mm/aaaa): ")
        fone = input("Telefone: ")

        tripulante = {
            "Nome": nome,
            "Cargo": cargo,
            "Idade": idade,
            "Admissão": data_admissao,
            "Fone": fone
        }
        tripulacao.append(tripulante)
        print("Tripulante cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar tripulante: {e}")

def imprimir_relatorios():
    print("\n--- Relatório de Clientes ---")
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. {cliente}")

    print("\n--- Relatório de Passagens ---")
    for i, passagem in enumerate(passagens, 1):
        print(f"{i}. {passagem}")

    print("\n--- Relatório de Aviões ---")
    for i, aviao in enumerate(avioes, 1):
        print(f"{i}. {aviao}")

    print("\n--- Relatório de Tripulação ---")
    for i, tripulante in enumerate(tripulacao, 1):
        print(f"{i}. {tripulante}")
menu_principal()