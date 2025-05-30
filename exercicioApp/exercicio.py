listaDeListas=[]



while True:
    userLista = []
    try:
        nome = (input("digite o seu nome: "))
    except:
        print("apenas letras!")
    while True:
        try:
            idade = (input('Idade: '))
            if idade.isdigit() and len(idade) == 1 or len(idade) == 2:
                break
            else:
                print('Digite uma idade válida!')
        except ValueError:
            print('Digite uma idade válida!')
    while True:
        sexo = input("digite o seu sexo (F ou M): ").lower()
        if sexo == "f" or sexo == "m":
            break
        else:
            print("ta errado")
    while True:
        cpf = (input("cpf: "))
        if len(cpf) < 11 or len(cpf) > 11:
            print("CPF inválido")
        else:
            break
    try:
        endereco = input("digite o seu endereço: ")
    except:
        print("apenas letras!")
    try:
        cidade = input("digite o sua cidade: ")
    except:
        print("apenas letras!")
    try:
        estado = input("digite o seu estado: ")
    except:
        print("apenas letras!")
    userLista.append(nome)
    userLista.append(idade)
    userLista.append(sexo)
    userLista.append(cpf)
    userLista.append(endereco)
    userLista.append(cidade)
    userLista.append(estado)
    listaDeListas.append(userLista)
    with open("exercicioApp/arquivo.txt","w") as arquivo:
        for pessoa in listaDeListas:
            linha = ", ".join([str(item) for item in pessoa])
            arquivo.write(linha + "\n")
    acao = int(input("1. para cadastrar mais uma pessoa\n2. para consultar o banco\n3. para encerrar\nescolha: "))
    if acao == 1:
        continue

    elif acao == 3:
        print("fim")
        break
    