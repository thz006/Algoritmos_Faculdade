produtos = {
    10: {"nome": "Caderno", "estoque": 0},
    20: {"nome": "Caneta", "estoque": 0},
    30: {"nome": "Lápis", "estoque": 0},
    40: {"nome": "Borracha", "estoque": 0},
    50: {"nome": "Régua", "estoque": 0}
}

def entrada_estoque():
    codigo = int(input("Código do produto para entrada: "))
    if codigo in produtos:
        qtd = int(input("Quantidade a entrar: "))
        produtos[codigo]["estoque"] += qtd
    else:
        print("Código inválido!")

def saida_estoque():
    codigo = int(input("Código do produto para saída: "))
    if codigo in produtos:
        qtd = int(input("Quantidade a sair: "))
        if produtos[codigo]["estoque"] >= qtd:
            produtos[codigo]["estoque"] -= qtd
        else:
            print("Estoque insuficiente para essa saída!")
    else:
        print("Código inválido!")

def relatorio():
    print("\nRelatório de Estoque Atual:")
    print("-" * 30)
    for codigo, dados in produtos.items():
        print(f"{dados['nome']}: {dados['estoque']} unidades")
    print("-" * 30)

# Programa principal
while True:
    print("\nEscolha a operação:")
    print("E – Entrada no estoque")
    print("S – Saída no estoque")
    print("R – Relatório")
    print("X – Sair")
    
    opcao = input("Opção: ").strip().upper()
    
    if opcao == "E":
        entrada_estoque()
    elif opcao == "S":
        saida_estoque()
    elif opcao == "R":
        relatorio()
    elif opcao == "X":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")
