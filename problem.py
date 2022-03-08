"""
The code in this module rebuilds Wordle. SCORING is the main function for assessing guesses.

Outstanding
- Enforce dictionary of five letter words for guesses and solutions
- Option to use random blank word
- Secret word:
  Blank = None
  r = Random
  Other = enforce five letter word from big list.
"""


def secret_input(secret_word):
    if secret_word == "":
        secret_provided = True
    else:
        secret_provided = False
        secret_word = secret_word
    return secret_provided


round = 0
keep_going = True
guesses = []


def scoring(guess, secret_word):
    score = [None, None, None, None, None]
    working_guess = list(guess)
    working_secret = list(secret_word)

    for letter in range(0, len(working_guess)):
        if working_guess[letter] == working_secret[letter]:
            score[letter] = "G"
            working_guess[letter] = None
            working_secret[letter] = None

    for letter in range(0, len(working_guess)):
        if working_guess[letter] == None:
            continue
        elif working_guess[letter] not in working_secret:
            score[letter] = "-"
            working_guess[letter] = None

    for letter in range(0, len(working_guess)):
        if working_guess[letter] == None:
            continue
        elif working_guess[letter] in working_secret:
            score[letter] = "Y"
            ws_index = working_secret.index(working_guess[letter])
            working_secret[ws_index] = None
            working_guess[letter] = None
        else:
            score[letter] = "-"
    score = ''.join(score).lower()
    return score


def keep_going_check(round, score):
    if score == "GGGGG":
        keep_going = False
        victory = True
    elif round == 6:
        keep_going = False
        victory = False
    else:
        keep_going = True
        victory = False
    return keep_going, victory


def game_loop():
    while keep_going is True:
        round += 1
        print('─' * 50)
        print(f"Round {round}")
        guess = input("Guess: ").upper()
        guesses.append(guess)
        score = scoring(guess, secret_word)
        print(f"Score: {score}")
        keep_going_che = keep_going_check(round, score)
        keep_going = keep_going_che[0]
        victory = keep_going_che[1]


def conclusion(victory, round, secret_word):
    if victory is True:
        print(f"Congratulations, you completed the puzzle in {round} guesses.")
        print(f"You guessed: {', '.join(guesses).upper()}")
        print(f"The secret word was: {secret_word.upper()}")
    else:
        print("You did not complete the game within 6 rounds.")
        print(f"You guessed: {guesses}")
        print(f"The secret word was: {secret_word}")


# def scoring_old(guess, secret_word):
#   score = []
#   for letter in range(0, len(guess)):
#     if guess[letter] == secret_word[letter]:
#       score.append("G")
#     elif guess[letter] not in list(secret_word):
#       score.append("-")
#     else:
#       score.append("Y")
#   return score
