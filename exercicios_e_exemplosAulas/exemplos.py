# nota1 = float(input("nota1: "))
# nota2 = float(input("nota2: "))
# media = (nota1 + nota2) / 2
# if media >= 7 and media <10:
#     print("aprovado")
# elif media < 7:
#     print("reprovado")
# elif media == 10:
#     print("aprovado com distinção")
lista=[]
for i in range(1,3):
    nota = float(input("nota: "))
    lista.append(nota)
media = sum(lista) / len(lista)
if media >= 7 and media <10:
    print("aprovado")
elif media < 7:
    print("reprovado")
elif media == 10:
    print("aprovado com distinção")