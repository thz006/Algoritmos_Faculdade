def data_valida(dia, mes, ano):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= mes <= 12:
        if 1 <= dia <= dias_mes[mes - 1]:
            return True
    return False