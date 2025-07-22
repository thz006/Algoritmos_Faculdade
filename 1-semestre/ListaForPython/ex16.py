n = int(input("numero de termos:  "))
lista = [1, 1]
for i in range(2, n):
    proximo = lista[i-1] + lista[i-2]
    lista.append(proximo)
print(lista[:n])