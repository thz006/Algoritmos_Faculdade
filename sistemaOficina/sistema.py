listaDeClientes=[]
def cadastrarCliente():
    while True:
        try:
            cpf=int(input("digite o CPF: "))
            break
        except ValueError:
            print("CPF inválido.")
    while True:
        try:
            nome=input("digite o nome: ")
            break
        except:
            print("nome inválido.")
    while True:
        try:
            telefone=int(input("digite o telefone: "))
            break
        except ValueError:
            print("Telefone inválido")

    cliente={'Nome': nome, 'cpf': cpf, 'telefone': telefone, 'veiculo': "", }
    listaDeClientes.append(cliente)
    with open("sistemaOficina/clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(str(f"\n{cliente}"))

    print("\nusuario cadastrado com sucesso.")

    print(listaDeClientes)

def cadastrarVeiculo():
    while True:
        try:
            placa=input("digite a placa: ")
            break
        except:
            print("placa inválida.")
    while True:
        try:
            modelo=input("digite o modelo: ")
            break
        except:
            print("modelo inválido")
    while True:
        try:
            ano=int(input("digite o ano do veículo: "))
            break
        except ValueError:
            print("Ano inválido")
    veiculovar= (f"placa: {placa}, modelo: {modelo}, ano: {ano}")
    veiculo={'placa': placa, 'modelo': modelo, 'ano': ano}

    

    while True:
        try:
            cpf=int(input("digite o CPF do proprietário: "))
            for cliente in listaDeClientes:
                if cliente['cpf'] == cpf:
                    cliente['veiculo'] = veiculovar
                    print(cliente)
                    with open("sistemaOficina/veiculos.txt", "a", encoding="utf-8") as arquivo:
                        arquivo.write(str(f"\n{veiculo}"))
                        
                    with open("sistemaOficina/cliente.txt", "w", encoding="utf-8") as arquivo:
                        arquivo.write(str(f"\n{cliente}"))
        except ValueError:
            print("CPF inválido.")

while True:
    def sistema():
        print("Bem Vindo ao sistema da Oficina.")
        print("Escolha uma opção de Ação: \n1.Cadastro\n2.Buscar dados\n3.Editar\n4.Excluir\n5.Sair\n")
        acao = int(input("digite a ação desejada: "))
        if acao == 1:
            print("Escolha oque você deseja cadastrar:\n1.Cadastrar cliente\n2.Cadastrar Veículo\n3.Cadastrar Ordem de Serviço\n4.Sair")
            acao2=int(input("Escolha: "))
            if acao2 == 1:
                cadastrarCliente()
            elif acao2 == 2:
                cadastrarVeiculo()
    sistema()