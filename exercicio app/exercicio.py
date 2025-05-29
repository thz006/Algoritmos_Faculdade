lista=[]




while True:
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
            print("TA CERTO")
        else:
            print("ta errado")
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
    