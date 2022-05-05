#Board vai ser uma matriz 3x3 na qual a posição preenchida
#será representada por 'X' e 'O'
def create_board():
    board = [['']*3 for n in range(0,3)]
    return board
# As posições serão passadas pelos jogadores
# Ex: 1 1 --> Linha 1 e Coluna 1

def fill_board(board, i, j, player):
    if player == 1:
        board[i - 1][j - 1] = 'X'
    else:
        board[i - 1][j - 1] = 'O'

# Queremos que a board apareça no terminal da seguinte forma:

#   1   2   3
# 1 X   O   X
# 2 X   O   O
# 3 O   X   O

def print_board(board):
    print('\t1\t2\t3')
    for i in range(0, 3):
        print(f'{i+1}\t{board[i][0]}\t{board[i][1]}\t{board[i][2]}')

# Agora que temos board totalmente preenchida (ou em partes preenchida), vamos determinar o vencedor, se houver.
# Como o player 1 sempre começa, ele terá 5 X e o segundo jogador 4 O.

# Vai procurar se há um vencedor após cada jogada.

def winner_number(board):
    # Analisando as linhas
    for row in board:
        if(row.count('X') == 3):
            return 1
        elif(row.count('O') == 3):
            return 2
    # Analisando as colunas
    for j in range(0,3):
        if(board[0][j] == board[1][j] and board[0][j] == board[2][j]):
            if(board[0][j] == 'X'):
                return 1
            elif(board[0][j] == 'O'):
                return 2
    # Analisando as diagonais principal e secundária
    if(board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        if(board[0][0] == 'X'):
            return 1
        elif(board[0][j] == 'O'):
            return 2
    if(board[2][0] == board[1][1] and board[2][0] == board[0][2]):
        if(board[2][0] == 'X'):
            return 1
        elif(board[0][j] == 'O'):
            return 2
    return 0

def full_board(board):
    for row in board:
        for elem in row:
            if(elem == ''):
                return False
    return True

def play(board, player):
    print('\n')
    i = int(input("Linha: "))
    j = int(input("Coluna: "))
    print('\n')
    while not (0 < i <= 3) or not (0 < j <= 3):
        print('\n')
        i = int(input("Linha: "))
        j = int(input("Coluna: "))
        print('\n')
    while board[i - 1][j - 1] != '':
        print('\n')
        i = int(input("Linha: "))
        j = int(input("Coluna: "))
        print('\n')
    fill_board(board,i,j,player)
    print_board(board)

