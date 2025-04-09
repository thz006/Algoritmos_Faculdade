print("-- Reservatório de Água --")  ### faltou o parêntese de fechamento

altura = float(input("Digite a altura (cm): "))  
largura = int(input("Digite a largura (cm): "))  ###parêntese de fechamento após o input
comprimento = float(input("Digite o comprimento (cm): "))  ### mesmo erro de cima
c_diario = float(input("Digite o valor do consumo médio diário (litros/dia): "))  ### faltando o = entre c_diario e o float()

## vírgula errada, deveria ser multiplicação
cap_total = (altura * largura * comprimento) / 1000  ## vírgula no lugar do operador de multiplicação

# Autonomia é capacidade total dividida pelo consumo diário
auton_reser = cap_total / c_diario

print("Capacidade do Reservatório = ", cap_total, "litros")
print("Autonomia do reservatório = ", auton_reser, "dias")  ### comentário de múltiplas linhas não pode ser usado após o print

# Classificação do consumo
if auton_reser < 2:
    print("Consumo Elevado")
elif auton_reser >= 2 and auton_reser <= 7:  ## condição digitada errada "auton_reser7"
    print("Consumo Moderado")
elif auton_reser > 7:
    print("Consumo Baixo")  ## caractere invisível no início do print (provavelmente um caractere especial/copypaste)
