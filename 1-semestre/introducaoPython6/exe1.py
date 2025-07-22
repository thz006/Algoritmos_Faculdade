# Função para capturar os dados do paciente
def capturar_dados():
    dados = {}

    dados["nome"] = input("Nome: ")
    dados["cpf"] = input("CPF: ")
    dados["rg"] = input("RG: ")
    dados["data_nascimento"] = input("Data de nascimento (dd/mm/aaaa): ")
    dados["sexo"] = input("Sexo (M/F): ")
    dados["peso"] = input("Peso (kg): ")
    dados["tipo_sanguineo"] = input("Tipo sanguíneo: ")
    dados["renda"] = input("Renda mensal: ")
    dados["endereco"] = input("Endereço: ")
    dados["telefone"] = input("Telefone: ")
    dados["cidade"] = input("Cidade: ")
    dados["estado"] = input("Estado: ")

    return dados

def imprimir_relatorio(dados):
    print("\n--- Relatório de Cadastro ---")
    print(f"Nome: {dados['nome']}")
    print(f"CPF: {dados['cpf']}")
    print(f"RG: {dados['rg']}")
    print(f"Data de Nascimento: {dados['data_nascimento']}")
    print(f"Sexo: {dados['sexo']}")
    print(f"Peso: {dados['peso']} kg")
    print(f"Tipo Sanguíneo: {dados['tipo_sanguineo']}")
    print(f"Renda Mensal: R$ {dados['renda']}")
    print(f"Endereço: {dados['endereco']}")
    print(f"Telefone: {dados['telefone']}")
    print(f"Cidade: {dados['cidade']}")
    print(f"Estado: {dados['estado']}")

dados_paciente = capturar_dados()
imprimir_relatorio(dados_paciente)
