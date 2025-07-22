def contar_elementos(lista):
    return {x: lista.count(x) for x in set(lista)}