media=0
soma=0
contador=1
for i in range(1,6):
    nota=float(input("nota: "))
    soma+=nota
    media=media+nota
    armazenarMedia=(media/contador)
    contador+=1

print(soma,"\n",armazenarMedia)