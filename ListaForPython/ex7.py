quant=int(input("quantidade de números: "))
maior=float('-inf')
menor=float('inf')
soma=0
for i in range(quant):
    numero=int(input("numero: "))
    if numero > maior:
        maior=numero
    if numero < menor:
        menor=numero
    soma+=numero
print(f"\n\n\nmaior: {maior}\nmenor: {menor}\nsoma: {soma}")