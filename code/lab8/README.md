## Exercise 1

Write a function ```makeGroceryList``` that takes a list of strings as its input. It should return a “grocery list”, which is a single string that separates the elements of the list with the word “and”.

    > makeGroceryList(['bananas', 'celery', 'apples', 'salt'])
    'bananas and celery and apples and salt'

## Exercise 2

Write a function ```makeTodaysGroceryList``` that takes a list of strings as its first argument and a predicate function as its second argument. It should return a “grocery list”, which identifies the elements of the list that satisfy the predicate, and then separates those elements with the word “and”.

    > def isPlural(s):
        return s.endswith('s')

    > makeTodaysGroceryList(['bananas', 'apples', 'salt'], isPlural)
    'bananas and apples'

## Exercise 3

Write a function ```drawBoard``` that takes a length-3 list of length-3 lists and prints out an attractive tic-tac-toe board.

    > drawBoard([["X", " ", "O"], [" ", "X", "O"], [" ", " ", "X"]])
    X| |O
    -+-+-
     |X|O
    -+-+-
     | |X

## Exercise 4

Write a function ```emptyBoard``` that creates an empty “board” (i.e. list of lists). Then write a function ```play``` that takes a board (list of lists), player (“X” or “O”), and grid location (from 1 to 9). It should modify the board to put that player’s symbol in the right location.

    > board = emptyBoard()
    > drawBoard(board)
     | |
    -+-+-
     | |
    -+-+-
     | |
    > play(board, "X", 5)
    > play(board, "O", 3)
    > drawBoard(board)
     | |O
    -+-+-
     |X|
    -+-+-
     | |


## Exercise 5

Write a function ```isFull``` that takes a board (list of lists), and returns ```True``` if all the squares contains either an X or an O.

    > board = [["X", " ", "O"],
               [" ", "X", "O"],
               [" ", " ", "X"]]

    > isFull(board)
    False

    > board = [["X", "X", "O"],
               ["O", "O", "O"],
               ["X", "O", "X"]]

    > isFull(board)
    True

## Exercise 6 

Write a function ```winner``` that takes a board (list of lists), and a player (“X” or “O”), and returns ```True``` if that player has already won the game (otherwise ```False```).

    > board = [["X", " ", "O"],
               [" ", "X", "O"],
               [" ", " ", "X"]]

    > winner(board, "X")
    True
    
    > winner(board, "O")
    False


## Exercise 7

Write a function ```tictactoe()``` that allows two players to play the game of tic-tac-toe.

    > tictactoe()
     | |
    -+-+-
     | |
    -+-+-
     | |
    Player X, please select a square: 5
     | |
    -+-+-
     |X|
    -+-+-
     | |
    Player O, please select a square: 8
     | |
    -+-+-
     |X|
    -+-+-
     |O|
    Player X, please select a square: 9
     | |
    -+-+-
     |X|
    -+-+-
     |O|X
    Player O, please select a square: 7
     | |
    -+-+-
     |X|
    -+-+-
    O|O|X
    Player X, please select a square: 1
    X| |
    -+-+-
     |X|
    -+-+-
    O|O|X

    X wins!

## Exercise 8

Extend the game so that players can engage in psychological warfare by rotating the board counterclockwise 90 degrees.

    > tictactoe()
     | |
    -+-+-
    | |
    -+-+-
    | |
    Player X, please select a square: 1
    X| |
    -+-+-
    | |
    -+-+-
    | |
    Player O, please select a square: 2
    X|O|
    -+-+-
    | |
    -+-+-
    | |
    Player X, please select a square: WARFARE
    | |
    -+-+-
    O| |
    -+-+-
    X| |
    Player X, please select a square: 1
    X| |
    -+-+-
    O| |
    -+-+-
    X| |
    Player O, please select a square:

If you finish, create an AI to play against.