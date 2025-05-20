estoque = {
    "arroz": 20,
    "feijão": 15,
    "macarrão": 30,
    "açúcar": 10,
    "café": 5
}

produto = input("Digite o nome do produto que deseja verificar: ").lower()

if produto in estoque:
    print(f"Temos {estoque[produto]} unidade(s) de {produto} em estoque.")
else:
    print(f"O produto '{produto}' não está disponível.")
