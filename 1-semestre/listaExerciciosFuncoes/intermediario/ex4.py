def substituir_vogais(s):
    return ''.join("*" if c.lower() in "aeiou" else c for c in s)