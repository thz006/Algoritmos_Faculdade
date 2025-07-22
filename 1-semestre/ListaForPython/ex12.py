codigos = [1, 2, 3, 4, 5]
veiculos = [1500, 3000, 2000, 1800, 2200]
acidentes = [12, 45, 20, 30, 25]

indices = [acidentes[i] / veiculos[i] for i in range(len(codigos))]

maior_indice_valor = max(indices)
menor_indice_valor = min(indices)
maior_indice_cidade = codigos[indices.index(maior_indice_valor)]
menor_indice_cidade = codigos[indices.index(menor_indice_valor)]

media_veiculos = sum(veiculos) / len(veiculos)

acidentes_menor_2000 = [
    acidentes[i] for i in range(len(veiculos)) if veiculos[i] < 2000
]
media_acidentes_menor_2000 = (
    sum(acidentes_menor_2000) / len(acidentes_menor_2000)
    if acidentes_menor_2000 else 0
)

(maior_indice_cidade, maior_indice_valor, menor_indice_cidade, menor_indice_valor,
 media_veiculos, media_acidentes_menor_2000)
