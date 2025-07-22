def acumulador():
    total = 0
    def interno(valor):
        nonlocal total
        total += valor
        return total
    return interno