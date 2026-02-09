def createplayers():
    player1 = [0] * 7
    player2 = [0] * 7
    return player1, player2

def createboard():
    # 0 : normal, 1 : Double Letter, 2 : Triple Letter, 3 : Double Word, 4 : Triple Word, 5 : Center
    board = [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4,
             0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0,
             0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0,
             1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1,
             0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
             0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0,
             0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
             4, 0, 0, 1, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 4,
             0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0,
             0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0,
             0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
             1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1,
             0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0,
             0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0,
             4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4,
             ]

    return board

def createbag():
    bag = [" ", " ",
           "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
           "A", "A", "A", "A", "A", "A", "A", "A", "A",
           "I", "I", "I", "I", "I", "I", "I", "I", "I",
           "O", "O", "O", "O", "O", "O", "O", "O",
           "N", "N", "N", "N", "N", "N",
           "R", "R", "R", "R", "R", "R",
           "T", "T", "T", "T", "T", "T",
           "D", "D", "D", "D",
           "L", "L", "L", "L",
           "S", "S", "S", "S",
           "U", "U", "U", "U",
           "G", "G", "G",
           "B", "B",
           "C", "C",
           "M", "M",
           "P", "P",
           "F", "F",
           "H", "H",
           "V", "V",
           "W", "W",
           "Y", "Y",
           "K",
           "J",
           "X",
           "Q",
           "Z", ]

    letter_id = {
        ' ': 0,
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    points = {
        ' ': 0,
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2,
        'h': 4,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10,
    }

    return bag, letter_id, points

def creategame():
    player1, player2 = createplayers()
    board = createboard()
    bag, letter_id, points = createbag()

    return player1, player2, board, bag, letter_id, points

def draw_board(board):
    print("\nDrawing the board...\n")


def play():
    # Init the game
    player1, player2, board, bag, letter_id, points = creategame()

    # print hands, board, bag
    print("\nplayer 1 :\n", player1)
    print("\nplayer 2 :\n", player2)
    print("\nboard :\n", board)
    print("\nbag :\n", bag)
    print("\nletter_id :\n", letter_id)
    print("\npoints :\n", points)


    # While the game is not finished (bag empty + one player without tiles OR no move possible)

            # The two players draw their hands (Player 1 THEN Player 2)

            # Brutforce to know the best play for player 1

            # Player1 plays it

            # Increment P1 score

            # Player1 draw until 7 tiles

            # Brutfoce to know the play for player 2

            # Player 2 plays

            # Increment P2 score

            # Player2 draw until 7 tiles

            # Print hands, board, bag





play()

