def validar_sudoku(tabuleiro):
    for i in range(9):
        linha = set()
        coluna = set()
        bloco = set()
        for j in range(9):
            linha.add(tabuleiro[i][j])
            coluna.add(tabuleiro[j][i])
            bloco.add(tabuleiro[3*(i//3) + j//3][3*(i%3) + j%3])
        if len(linha) != 9 or len(coluna) != 9 or len(bloco) != 9:
            return False
    return True