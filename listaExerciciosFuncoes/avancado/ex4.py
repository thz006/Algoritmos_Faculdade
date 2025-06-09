def contar_palavras_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        texto = f.read()
    return len(texto.split())