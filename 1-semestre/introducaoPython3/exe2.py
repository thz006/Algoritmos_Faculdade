nome= str(input("nome: "))
quant= int(input("quantidade: "))
val_unit= float(input("valor: "))
val_a_pagar = quant * val_unit
desc = float(input("desconto: "))
desc_result = (desc / 100) * val_a_pagar
total = val_a_pagar - desc_result
print(f"nome: {nome} \n quantidade: {quant} \n valor unitário: {val_unit} \n desconto: {desc} \n total: {total}")