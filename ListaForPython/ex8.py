from itertools import count
media=[]
for i in count():
    idade=int(input("idade: "))
    print("digite -1 para sair")
    media.append(idade)
    if idade == -1:
        break
mediaCalc=sum(media)/len(media)
print(f"media: {mediaCalc}")
if mediaCalc >= 0 and mediaCalc <= 25:
    print("jovem")
elif mediaCalc >= 25 and mediaCalc <=60:
    print("adulta")
elif mediaCalc > 60:
    print("idosa")
