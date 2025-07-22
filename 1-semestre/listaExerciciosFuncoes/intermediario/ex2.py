def soma_dos_digitos(n):
    return sum(int(d) for d in str(abs(n)))