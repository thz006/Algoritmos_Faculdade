def segundo_maior(lista):
    lista = list(set(lista))
    lista.sort(reverse=True)
    return lista[1] if len(lista) >= 2 else None