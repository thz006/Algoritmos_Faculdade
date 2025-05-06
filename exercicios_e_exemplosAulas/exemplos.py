listaClientes=[]

print("\nBem Vindo ao Banco!\n")
while True:
    print("Ações disponíveis:\n \n 1- Cadastrar Cliente\n 2- Consultar saldo\n 3- Fazer depósito\n 4- Fazer saque\n")
    print("digite o número respectivo a ação desejada\n")
    acao = int(input("Ação: "))
    if acao == 1:
        Cliente=[]
        print("\nPara cadastrar o cliente, informe os seguintes dados: \n")
        nome = input("Nome: ")
        cpf = int(input("CPF: "))
        rg = int(input("RG: "))
        telefone = int(input("Telefone: "))
        NumAgencia = int(input("Número da agência: "))
        NumConta = int(input("Número conta: "))
        saldo = float(input("Saldo Inicial: "))
        Cliente.append(nome)
        Cliente.append(cpf)
        Cliente.append(rg)
        Cliente.append(telefone)
        Cliente.append(NumAgencia)
        Cliente.append(NumConta)
        Cliente.append(saldo)
        listaClientes.append(Cliente)
        print(f"Clientes cadastrados: \n{listaClientes}")
        print(f"\n{nome}, seu cadastro foi realizado com sucesso!")
    elif acao == 2:
        print("Digite o CPF do cliente que você deseja consultar o saldo\n")
        buscaCPF = int(input("CPF: "))
        for i in listaClientes:
            for cpf in i:
                if cpf == buscaCPF:
                    print(f"Saldo de {i[0]}: {i[6]} reais")