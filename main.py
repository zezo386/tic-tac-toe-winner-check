def tic_tac_toe(board:list):
    for i in range(3):
            if board[i*3] == board[(i*3)+1] == board[(i*3)+2]:
                return f"{board[i*3]} wins! by horizantal"
            if board[i]==board[i+3]==board[i+6]:
                return f"{board[i]} wins!"
            if (board[0]==board[4]==board[8]) or (board[2]==board[4]==board[6]):
                return f"{board[4]} wins!"
    return "Draw"

#
print(tic_tac_toe(["X","O","X",
                   "O","X","X",
                   "X","O","O"]))