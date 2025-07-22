temperaturas = []
meses = []
anos = []
while True:
    temp = float(input("Digite a temperatura (ou -999 para sair): "))
    if temp == -999:
        break
    mes = input("Digite o mês em que ocorreu: ")
    ano = input("Digite o ano em que ocorreu: ")
    
    temperaturas.append(temp)
    meses.append(mes)
    anos.append(ano)

if len(temperaturas) == 0:
    print("Nenhuma temperatura foi informada.")
else:
    menor = temperaturas[0]
    maior = temperaturas[0]
    idx_menor = 0
    idx_maior = 0
    soma = 0
    for i in range(len(temperaturas)):
        if temperaturas[i] < menor:
            menor = temperaturas[i]
            idx_menor = i
        if temperaturas[i] > maior:
            maior = temperaturas[i]
            idx_maior = i
        soma += temperaturas[i]
    media = soma / len(temperaturas)
    print("\nRESULTADOS:")
    print(f"Menor temperatura: {menor}°C em {meses[idx_menor]}/{anos[idx_menor]}")
    print(f"Maior temperatura: {maior}°C em {meses[idx_maior]}/{anos[idx_maior]}")
    print(f"Média das temperaturas: {media:.2f}°C")
