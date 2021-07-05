def hangman():
    word = 'antonio'
    wrong_guesses = 0
    stage = [ "" , "________ " , "| | " , "| 0 " , "| /|\ " , "| / \ " , "| " ]
    score_board = ['_ '] * len(word)
    letter_left = list(word)
    win = False
    print('Welcome to the game!')

    while wrong_guesses < len(stage) - 1:
        print (' \n ')
        guess = input('Guess a letter: ')
        if guess in letter_left:
            index_guessed = letter_left.index(guess)
            score_board[index_guessed] = guess
            letter_left[index_guessed] = '$'
        else:
            wrong_guesses += 1
        print(''.join(score_board))
        print('\n'.join(stage[0:wrong_guesses + 1]))
        if not '_ ' in score_board:
            win = True
            print('You won de game!')
            print('The word to guess was {}'.format(word))
            break
    if not win:
        print('\n'.join(stage[0:wrong_guesses + 1]))
        print('You lose de game!')
        print('The correct word was {}'.format(word))

hangman()