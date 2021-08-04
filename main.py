



play = input('Would you like to play Tic Tac Toe? y or n: ')

while play == "y":
    t = {
        'a1': " ",
        'a2': " ",
        'a3': " ",
        'b1': " ",
        'b2': " ",
        'b3': " ",
        'c1': " ",
        'c2': " ",
        'c3': " "
    }

    current_player = 1

    def check_results():
        if t["a1"] == t['a2'] and t['a2'] == t['a3'] and t['a1'] != " ":
            return t['a1']
        elif t["b1"] == t['b2'] and t['b2'] == t['b3'] and t['b1'] != " ":
            return t['b1']
        elif t["c1"] == t['c2'] and t['c2'] == t['c3'] and t['c1'] != " ":
            return t['c1']
        elif t["a1"] == t['b1'] and t['b1'] == t['c1'] and t['a1'] != " ":
            return t['a1']
        elif t["a2"] == t['b2'] and t['b2'] == t['c2'] and t['a2'] != " ":
            return t['a2']
        elif t["a3"] == t['b3'] and t['b3'] == t['c3'] and t['a3'] != " ":
            return t['a3']
        elif t['a1'] == t['b2'] and t['b2'] == t['c3'] and t['a1'] != " ":
            return t['a1']
        elif t['a3'] == t['b2'] and t['b2'] == t['c1'] and t['a3'] != " ":
            return t['a3']

    def check_draw():
        empty = 0
        for i in t:
            if t[i] != " ":
                empty += 1
        if empty == 9:
            return True



    on = True
    while on:

        print('  1   2   3\n'
            f'a {t["a1"]} | {t["a2"]} | {t["a3"]}\n'
              '  ---------\n'
              f'b {t["b1"]} | {t["b2"]} | {t["b3"]}\n'
              '  ---------\n'
              f'c {t["c1"]} | {t["c2"]} | {t["c3"]}\n'
              )



        if current_player == 1:
            player_1_choice = input('Where would you like you like to place X?')
            t[player_1_choice] = "X"
            current_player = 0
        elif current_player == 0:
            player_2_choice = input('Where would you like you like to place O?')
            t[player_2_choice] = "O"
            current_player = 1

        if check_results() == "X":
            print("X wins!")
            on = False
        elif check_results() == "O":
            print("O wins!")
            on = False
        elif check_draw():
            print("Draw!")
            on = False

    #restarts the game if needed
    play_again = input("Would you like to play again? y or n: ")
    if play_again == "n":
        play = "n"






