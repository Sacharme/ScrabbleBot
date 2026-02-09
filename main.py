import random
import math
from datetime import datetime


def createplayers():
    player1 = [-1] * 7
    player2 = [-1] * 7
    return player1, player2


def createscores():
    scores = {
        "player1": 0,
        "player2": 0,
    }

    return scores


def createboard():
    # 0 : normal, 1 : Double Letter, 2 : Triple Letter, 3 : Double Word, 4 : Triple Word, 5 : Center
    board = [[4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4],
             [0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0],
             [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0],
             [1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1],
             [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
             [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [4, 0, 0, 1, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 4],
             [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
             [0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
             [1, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1],
             [0, 0, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 3, 0, 0],
             [0, 3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0],
             [4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 4],
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
        None: -1,
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
    scores = createscores()
    board = createboard()
    bag, letter_id, points = createbag()

    # print hands, board, bag
    print("\nHand of player 1 :\n", player1)
    print("\nHand of player 2 :\n", player2)
    print("\nScores :\n", scores)
    print("\nBoard :\n", board)
    print("\nBag :\n", bag)
    print("\nletter_id :\n", letter_id)
    print("\npoints :\n", points)

    return player1, player2, scores, board, bag, letter_id, points


def draw_board(board):
    print("\nDrawing the board...\n")


def process_wordlist(words):
    print("\nProcessing the list of words...\n")

    # Go trough the whole list
    for word in words:
        # if a word begins with a capital letter or is one letter long, remove it
        if word[0].isLower() or len(word) <= 1:
            words.pop(word)

    return words


def pick_tiles(player1, player2, bag, max_len_hands):
    print("\nPicking tiles...\n")
    # While each player have less than 7 tiles
    # The two players draw their hands (Player 1 THEN Player 2)

    for i in range(max_len_hands):
        if player1[i] == -1:
            # Draw a new letter from bag
            player1[i] = random.choice(bag)

    for i in range(max_len_hands):
        if player2[i] == -1:
            # Draw a new letter from bag
            player2[i] = random.choice(bag)

    print("\nHand of player 1 :\n", player1)
    print("\nHand of player 2 :\n", player2)

    return player1, player2


def brut_force_play(player, board, nbr_possible_hands):
    print("\nBrut forcing the play...\n")
    combinaisons = [None] * nbr_possible_hands
    word = ""
    start = [0][0]
    direction = 0  # 0 : horizontale, 1 : verticale
    score = 0

    # Create every possible word that the player can make with its max_len_hands tiles (max_len_hands! possibilities)

    # Check 5k times
    # for i in range(nbr_possible_hands):
    #     #
    #     for letter in player:
    #        combinaisons chp quoi
    #
    #
    #

    return word, start, direction, score


def place_word(player, word, start, direction, board):
    print("\nPlacing the word...\n")

    # Add to board

    # Delete to player's hand


def play():
    # word_file = None
    # words = word_file.read().split("\n")
    # process_wordlist(words)

    # Init the game
    player1, player2, scores, board, bag, letter_id, points = creategame()

    # Variables
    randomseed = 42
    random.seed(datetime.now().timestamp())
    max_len_hands = 7
    nbr_possible_hands = math.factorial(max_len_hands)

    is_move_possible = True

    # While the game is not finished (bag empty + one player without tiles OR no move possible)
    while (len(bag) != 0 and (len(player1) != 0 or len(player2) != 0)) or is_move_possible == True:
        # Pick tiles
        player1, player2 = pick_tiles(player1, player2, bag, max_len_hands)

        # PLAYER 1 TURN

        # Brutforce to know the best play for player 1
        word, start, direction, score = brut_force_play(player1, board, nbr_possible_hands)

        # Player1 plays it (remove letter from hand and add letter to board)
        place_word(player1, word, start, direction, board)

        # Increment score
        scores[player1] += score

        # PLAYER 2 TURN

        # Brutfoce to know the play for player 2
        word, start, direction, score = brut_force_play(player2, board, nbr_possible_hands)

        # Player 2 plays (remove letter from hand and add letter to board)
        place_word(player2, word, start, direction, board)

        # Increment score
        scores[player2] += score

        # Print hands, board, bag
        print("\nHand of player 1 :\n", player1)
        print("\nHand of player 2 :\n", player2)
        print("\nboard :\n", board)
        print("\nbag :\n", bag)

    print(max(scores))


play()
