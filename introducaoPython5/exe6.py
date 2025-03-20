nome = str(input("nome: "))
i = list(nome)
if len(i) < 8:
    print("nome com menos de 8 caracteres!")
else:
    print(i[0:8])