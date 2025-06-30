import os

listaDeClientes = []

# cadastro
def cadastrarCliente():
    while True:
        try:
            cpf = int(input("Digite o CPF: "))
            if any(cliente['cpf'] == cpf for cliente in listaDeClientes):
                print("CPF já cadastrado.")
                return
            break
        except ValueError:
            print("CPF inválido.")
    nome = input("Digite o nome: ")
    while not nome.strip():
        nome = input("Nome inválido. Digite novamente: ")
    while True:
        try:
            telefone = int(input("Digite o telefone: "))
            break
        except ValueError:
            print("Telefone inválido.")

    cliente = {'nome': nome, 'cpf': cpf, 'telefone': telefone, 'veiculo': None}
    listaDeClientes.append(cliente)

    with open("sistemaOficina/clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(str(cliente) + "\n")

    print("\nUsuário cadastrado com sucesso.")
    print(listaDeClientes)

def cadastrarVeiculo():
    placa = input("Digite a placa: ").upper()
    modelo = input("Digite o modelo: ")
    while not modelo.strip():
        modelo = input("Modelo inválido. Digite novamente: ")
    while True:
        try:
            ano = int(input("Digite o ano do veículo: "))
            break
        except ValueError:
            print("Ano inválido.")

    veiculo = {'placa': placa, 'modelo': modelo, 'ano': ano}

    cpf = int(input("Digite o CPF do proprietário: "))
    for cliente in listaDeClientes:
        if cliente['cpf'] == cpf:
            cliente['veiculo'] = veiculo
            print("Veículo cadastrado com sucesso para o cliente:", cliente['nome'])
            with open("sistemaOficina/veiculos.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(str(veiculo) + "\n")
            with open("sistemaOficina/clientes.txt", "w", encoding="utf-8") as arquivo:
                for c in listaDeClientes:
                    arquivo.write(str(c) + "\n")
            return
    print("Cliente não encontrado.")

def cadastrarOS():
    try:
        numero = input("Número da OS: ")
        descricao = input("Descrição do serviço: ")
        valor = float(input("Valor do serviço: "))
        cpf = int(input("CPF do cliente: "))
        placa = input("Placa do veículo: ").upper()

        encontrado = False
        for cliente in listaDeClientes:
            if cliente['cpf'] == cpf and cliente['veiculo'] and cliente['veiculo']['placa'] == placa:
                os = {'numero': numero, 'descricao': descricao, 'valor': valor, 'cpf': cpf, 'placa': placa}
                with open("sistemaOficina/ordens_servico.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(str(os) + "\n")
                print("Ordem de serviço cadastrada com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Cliente ou veículo não encontrado.")
    except ValueError:
        print("Valor inválido.")

### consultar
def listarClientes():
    print("\n--- Clientes Cadastrados ---")
    try:
        with open("sistemaOficina/clientes.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhum cliente cadastrado ainda.")

def listarVeiculos():
    print("\n--- Veículos Cadastrados ---")
    try:
        with open("sistemaOficina/veiculos.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhum veículo cadastrado ainda.")

def listarOS():
    print("\n--- Ordens de Serviço ---")
    try:
        with open("sistemaOficina/ordens_servico.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Nenhuma OS cadastrada ainda.")

##Edita
def editarCliente():
    cpf = int(input("Digite o CPF do cliente a editar: "))
    for cliente in listaDeClientes:
        if cliente['cpf'] == cpf:
            cliente['nome'] = input("Novo nome: ")
            cliente['telefone'] = int(input("Novo telefone: "))
            with open("sistemaOficina/clientes.txt", "w", encoding="utf-8") as arquivo:
                for c in listaDeClientes:
                    arquivo.write(str(c) + "\n")
            print("Cliente atualizado com sucesso.")
            return
    print("Cliente não encontrado.")

###excluir
def excluirCliente():
    cpf = int(input("Digite o CPF do cliente a excluir: "))
    global listaDeClientes
    listaDeClientes = [c for c in listaDeClientes if c['cpf'] != cpf]
    with open("sistemaOficina/clientes.txt", "w", encoding="utf-8") as arquivo:
        for c in listaDeClientes:
            arquivo.write(str(c) + "\n")
    print("Cliente excluído com sucesso.")

def sistema():
    while True:
        print("\nBem-vindo ao sistema da Oficina.")
        print("Escolha uma opção:")
        print("1. Cadastrar\n2. Buscar dados\n3. Editar\n4. Excluir\n5. Sair")
        try:
            acao = int(input("Digite a ação desejada: "))
            if acao == 1:
                print("\n1. Cadastrar Cliente\n2. Cadastrar Veículo\n3. Cadastrar Ordem de Serviço\n4. Voltar")
                acao2 = int(input("Escolha: "))
                if acao2 == 1:
                    cadastrarCliente()
                elif acao2 == 2:
                    cadastrarVeiculo()
                elif acao2 == 3:
                    cadastrarOS()
            elif acao == 2:
                print("\n1. Listar Clientes\n2. Listar Veículos\n3. Listar OS")
                opcao = int(input("Escolha: "))
                if opcao == 1:
                    listarClientes()
                elif opcao == 2:
                    listarVeiculos()
                elif opcao == 3:
                    listarOS()
            elif acao == 3:
                editarCliente()
            elif acao == 4:
                excluirCliente()
            elif acao == 5:
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

if not os.path.exists("sistemaOficina"):
    os.makedirs("sistemaOficina")

sistema()
