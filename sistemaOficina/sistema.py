# Sistema Oficina sem importações complexas nem dict, zip ou estruturas difíceis

# Cadastro

def cadastrarCliente():
    cpf = input("CPF: ")
    try:
        with open("clientes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith(cpf + ";"):
                    print("CPF já cadastrado.")
                    return
    except:
        pass
    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    with open("clientes.txt", "a", encoding="utf-8") as f:
        f.write(cpf + ";" + nome + ";" + telefone + "\n")
    print("Cliente cadastrado.")

def cadastrarVeiculo():
    placa = input("Placa: ").upper()
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith(placa + ";"):
                    print("Placa já cadastrada.")
                    return
    except:
        pass
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cpf = input("CPF do proprietário: ")
    encontrado = False
    try:
        with open("clientes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith(cpf + ";"):
                    encontrado = True
                    break
    except:
        pass
    if not encontrado:
        print("Cliente não encontrado.")
        return
    with open("veiculos.txt", "a", encoding="utf-8") as f:
        f.write(placa + ";" + modelo + ";" + ano + ";" + cpf + "\n")
    print("Veículo cadastrado.")

def cadastrarOS():
    numero = input("Número da OS: ")
    descricao = input("Descrição: ")
    valor = input("Valor: ")
    cpf = input("CPF do cliente: ")
    placa = input("Placa do veículo: ").upper()
    cliente_ok = False
    veiculo_ok = False
    try:
        with open("clientes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith(cpf + ";"):
                    cliente_ok = True
                    break
    except:
        pass
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if linha.startswith(placa + ";"):
                    veiculo_ok = True
                    break
    except:
        pass
    if not cliente_ok:
        print("Cliente não encontrado.")
        return
    if not veiculo_ok:
        print("Veículo não encontrado.")
        return
    with open("ordens_servico.txt", "a", encoding="utf-8") as f:
        f.write(numero + ";" + descricao + ";" + valor + ";" + cpf + ";" + placa + "\n")
    print("OS cadastrada.")

# Exclusões simples

def excluirCliente():
    cpf = input("CPF do cliente a excluir: ")
    linhas = []
    try:
        with open("clientes.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        with open("clientes.txt", "w", encoding="utf-8") as f:
            for linha in linhas:
                if not linha.startswith(cpf + ";"):
                    f.write(linha)
    except:
        print("Erro ao excluir cliente.")

    # Excluir veículos e OS também
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as f:
            veiculos = f.readlines()
        with open("veiculos.txt", "w", encoding="utf-8") as f:
            for linha in veiculos:
                if not linha.strip().endswith(";" + cpf):
                    f.write(linha)
    except:
        pass

    try:
        with open("ordens_servico.txt", "r", encoding="utf-8") as f:
            ordens = f.readlines()
        with open("ordens_servico.txt", "w", encoding="utf-8") as f:
            for linha in ordens:
                if ";" + cpf + ";" not in linha:
                    f.write(linha)
    except:
        pass

    print("Cliente e dados relacionados excluídos.")

def excluirVeiculo():
    placa = input("Placa do veículo a excluir: ").upper()
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        with open("veiculos.txt", "w", encoding="utf-8") as f:
            for linha in linhas:
                if not linha.startswith(placa + ";"):
                    f.write(linha)
    except:
        print("Erro ao excluir veículo.")

def excluirOS():
    numero = input("Número da OS a excluir: ")
    try:
        with open("ordens_servico.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        with open("ordens_servico.txt", "w", encoding="utf-8") as f:
            for linha in linhas:
                if not linha.startswith(numero + ";"):
                    f.write(linha)
    except:
        print("Erro ao excluir OS.")

# Consulta por CPF e número

def consultarVeiculosPorCPF():
    cpf = input("Digite o CPF: ")
    try:
        with open("veiculos.txt", "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if dados[3] == cpf:
                    print(linha.strip())
    except:
        print("Erro ao consultar veículos.")

def consultarOS():
    chave = input("Digite o CPF ou número da OS: ")
    try:
        with open("ordens_servico.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if chave in linha:
                    print(linha.strip())
    except:
        print("Erro ao consultar OS.")

# Menu

def sistema():
    while True:
        print("\nMENU PRINCIPAL")
        print("1 - Cadastrar")
        print("2 - Excluir")
        print("3 - Consultar")
        print("4 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            print("1 - Cliente\n2 - Veículo\n3 - Ordem de Serviço")
            cad = input("Escolha: ")
            if cad == "1": cadastrarCliente()
            elif cad == "2": cadastrarVeiculo()
            elif cad == "3": cadastrarOS()

        elif opcao == "2":
            print("1 - Cliente\n2 - Veículo\n3 - Ordem de Serviço")
            esc = input("Escolha: ")
            if esc == "1": excluirCliente()
            elif esc == "2": excluirVeiculo()
            elif esc == "3": excluirOS()

        elif opcao == "3":
            print("1 - Veículos por CPF\n2 - OS por CPF ou número")
            con = input("Escolha: ")
            if con == "1": consultarVeiculosPorCPF()
            elif con == "2": consultarOS()

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

sistema()
