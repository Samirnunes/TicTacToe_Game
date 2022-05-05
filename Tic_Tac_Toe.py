#from Functions.Board import print_board,create_board, play, full_board, winner_number
from Functions import Board

board = Board.create_board()
Board.print_board(board)
while True:
    Board.play(board,1)
    winner = Board.winner_number(board)
    if winner == 1:
        print("\nJogador 1 venceu !")
        break
    elif winner == 2:
        print("\nJogador 2 venceu !")
        break
    if(Board.full_board(board)):
        print("\nEmpate !")
        break
    Board.play(board,2)
    winner = Board.winner_number(board)
    if winner == 1:
        print("\nJogador 1 venceu !")
        break
    elif winner == 2:
        print("\nJogador 2 venceu !")
        break
    if(Board.full_board(board)):
        print("\nEmpate !")
        break
    