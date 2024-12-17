def rock_paper_scissors(player1_choice, player2_choice):
    if player1_choice == 0:
        if player2_choice == 0:
            return 0
        elif player2_choice == 1:
            return 2
        else: return 1
    
    if player1_choice == 1:
        if player2_choice == 0:
            return 1
        elif player2_choice == 1:
            return 0
        else: return 2

    if player1_choice == 2:
        if player2_choice == 0:
            return 2
        elif player2_choice == 1:
            return 1
        else: return 0