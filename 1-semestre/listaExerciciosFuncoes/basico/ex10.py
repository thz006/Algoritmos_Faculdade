def contar_vogais(s):
    return sum(1 for c in s.lower() if c in "aeiou")