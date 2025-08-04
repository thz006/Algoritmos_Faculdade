ARQUIVO_PRODUTOS = "database/produtos.txt"

def salvar_produto_linha(produto):
    linha = ";".join([
        produto['codigo'],
        produto['nome'],
        produto['categoria'],
        produto['unidade'],
        str(produto['preco_custo']),
        str(produto['preco_venda']),
        str(produto['estoque']),
        str(produto['estoque_min']),
        str(produto['estoque_max'])
    ]) + "\n"
    
    with open(ARQUIVO_PRODUTOS, "a", encoding="utf-8") as f:
        f.write(linha)

def ler_produtos():
    produtos = []
    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(";")
                produto = {
                    'codigo': dados[0],
                    'nome': dados[1],
                    'categoria': dados[2],
                    'unidade': dados[3],
                    'preco_custo': float(dados[4]),
                    'preco_venda': float(dados[5]),
                    'estoque': int(dados[6]),
                    'estoque_min': int(dados[7]),
                    'estoque_max': int(dados[8])
                }
                produtos.append(produto)
    except FileNotFoundError:
        pass
    return produtos

def cadastrar_produto():
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    categoria = input("Categoria (elétrica, hidráulica, etc.): ")
    unidade = input("Unidade (kg, m², saco, etc.): ")
    preco_custo = float(input("Preço de custo (R$): "))
    preco_venda = float(input("Preço de venda (R$): "))
    estoque = int(input("Quantidade em estoque: "))
    estoque_min = int(input("Estoque mínimo: "))
    estoque_max = int(input("Estoque máximo: "))

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "unidade": unidade,
        "preco_custo": preco_custo,
        "preco_venda": preco_venda,
        "estoque": estoque,
        "estoque_min": estoque_min,
        "estoque_max": estoque_max
    }

    salvar_produto_linha(produto)
    print("✅ Produto cadastrado com sucesso!\n")

def listar_produtos():
    produtos = ler_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    print("\n📦 Lista de Produtos:")
    for p in produtos:
        print(f"[{p['codigo']}] {p['nome']} | Categoria: {p['categoria']} | Estoque: {p['estoque']} | Venda: R$ {p['preco_venda']:.2f}")
    print()

def produtos_estoque_baixo():
    produtos = ler_produtos()
    print("\n🚨 Produtos com Estoque Abaixo do Mínimo:")
    for p in produtos:
        if p['estoque'] < p['estoque_min']:
            print(f"{p['nome']} - Estoque atual: {p['estoque']} | Mínimo: {p['estoque_min']}")
    print()

def menu_produtos():
    while True:
        print("\n--- Menu de Produtos ---")
        print("1. Cadastrar novo produto")
        print("2. Listar todos os produtos")
        print("3. Ver produtos com estoque baixo")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            produtos_estoque_baixo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")