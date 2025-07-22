par=0
impar=0
for i in range(1,11):
    num=int(input("numero: "))
    if num % 2 == 0:
        par+=1
    elif num % 2 != 0:
        impar+=1
print(f"quantidade de pares: {par}\nquantidade de ímpares: {impar}")