listaDeClientes=()
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

    cliente={'Nome': nome, 'cpf': cpf, 'telefone': telefone}

    with open("sistemaOficina/clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(str(cliente))

    print("usuario cadastrado com sucesso.")

while True:
    def sistema():
        print("Bem Vindo ao sistema da Oficina.")
        print("Escolha uma opção de Ação: \n1.Cadastro\n2.Buscar dados\n3.Editar\n4.Excluir\n5.Sair\n")
        acao = int(input("digite a ação desejada: "))
        if acao == 1:
            cadastrarCliente()
    sistema()