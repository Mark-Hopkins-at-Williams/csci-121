def drawBoard(board):
    rows = []
    for i in range(3):
        rows.append("|".join(board[i]))
    print("\n-+-+-\n".join(rows))
    
def emptyBoard():
    return [[" "," "," "],[" "," "," "],[" "," "," "]]

def play(board, player, square):
    if square == "WARFARE":
        rotateLeft(board)
        return player
    else:
        square = int(square) - 1
        row = square // 3
        col = square % 3
        board[row][col] = player
        if player == "X":
            return "O"
        else:
            return "X"

def isFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def winner(board, player):
    def winningRow(board, player, row):
        for i in range(3):
            if board[row][i] != player:
                return False
        return True
    def winningCol(board, player, col):
        for i in range(3):
            if board[i][col] != player:
                return False
        return True 
    for i in range(3):
        if winningRow(board, player, i):
            return True
        elif winningCol(board, player, i):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False

def rotateLeft(array):
    newArray=[[0]*len(array) for i in range(len(array[0]))]
    for col in range(len(newArray[0])):
        for row in range(len(newArray)):
            newArray[row][col]=array[col][len(array[0])-1-row]
    for i in range(3):
        for j in range(3):            
            array[i][j] = newArray[i][j]
 
def tictactoe():
    board = emptyBoard()
    drawBoard(board)
    player = "X"
    while not winner(board, "X") and not winner(board, "O") and not isFull(board):
        response = input("Player {}, please select a square: ".format(player))
        player = play(board, player, response)        
        drawBoard(board)
    if winner(board, "X"):
        print("\nX wins!")
    elif winner(board, "O"):
        print("\nO wins!")
    else:
        print("\nStalemate!")