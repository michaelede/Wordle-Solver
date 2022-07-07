"""
The functions below deal with user guess inputs:
- guess_input:    prompts the user to enter their guess and  the guess score
- guess_scoring:  converts the guess into lists representing the position
     of green letters, yellow letters etc.
- big_filter:    filters the remaining word list for words compatible with
     the previous guess.
"""
from datetime import datetime

# Old colours: 🟨, 🟩, ⬛ )
results_colour = {
    "-": "⬛",
    "Y": "🟨",
    "G": "🟩"}


def guess_input():
    word_length = 0
    while word_length != 5:
        input_word = input("Type your guess:  ").lower()
        word_length = len(input_word)
        if word_length != 5:
            print("Must be a five letter word.")
    return input_word


def score_input():
    score_length = 0
    input_score = []

    while score_length != 5:
        input_score_base = input("Type the score:   ").lower()
        score_length = len(input_score_base)

        if score_length != 5:
            print("Must be a five letter score.")

    for letter in input_score_base:

        if letter == ".":
            input_score.append("g")
        elif letter == ",":
            input_score.append("y")
        elif letter == "/":
            input_score.append("-")
        else:
            input_score.append(letter)

    return "".join(input_score)


def score_colour(input_score):
    scores = list(input_score.upper())
    colour_score = []
    for item in scores:
        item_colour = results_colour.get(item)
        colour_score.append(item_colour)
    score_colour = "".join(colour_score)
    return score_colour


def printable_sequence(print_word, print_score, print_sequence):
    print_sequence_new = [print_word, print_score]
    print_sequence = print_sequence + print_sequence_new
    return print_sequence


def print_results(print_word, print_score):
    import modules
    modules.clear_row()
    modules.clear_row()
    print(f"             {print_word}")
    print(f"             {print_score}")


def guess_scoring(input_word, input_score, grey_letters):
    green_position = []
    yellow_position = []

    for letter in range(0, len(input_score)):

        if input_score[letter] == "g" or input_score[letter] == ".":
            green_position.append(input_word[letter])
            yellow_position.append(None)

        elif input_score[letter] == "y" or input_score[letter] == ",":
            green_position.append(None)
            yellow_position.append(input_word[letter])

        elif input_score[letter] == "-" or input_score[letter] == "/":
            green_position.append(None)
            yellow_position.append(None)
            grey_letters.append(input_word[letter])

        else:
            print("You have typed an invalid character.")

    return green_position, yellow_position, grey_letters


def five_greens(green_position):
    green_letters = list(filter(None, green_position))

    if len(green_letters) == 5:
        five_greens = True
    else:
        five_greens = False
    return five_greens


def green_filter(word_list, green_position):

    obey_greens = []

    for candidate in word_list:
        obey_green_test = True

        for letter in range(0, len(candidate)):

            if (green_position[letter] != candidate[letter]
                    and green_position[letter] is not None):
                obey_green_test = False

        if obey_green_test is True:
            obey_greens.append(candidate)

    return obey_greens


def yellow_letter_filter(word_list, yellow_position):
    yellow_letters = list(filter(None, yellow_position))
    obey_yellow_letters = []

    for candidate in word_list:
        obeyYellowLetterTest = True

        for letter in range(0, len(yellow_letters)):

            if (yellow_letters[letter] not in candidate):
                obeyYellowLetterTest = False

        if (obeyYellowLetterTest is True):
            obey_yellow_letters.append(candidate)

    return obey_yellow_letters


def yellow_position_filter(word_list, yellow_position):
    obey_yellow_position = []

    for candidate in word_list:
        obey_yellow_position_test = True

        for letter in range(0, len(candidate)):

            if (yellow_position[letter] == candidate[letter]
                    and yellow_position[letter] is not None):
                obey_yellow_position_test = False

        if (obey_yellow_position_test is True):
            obey_yellow_position.append(candidate)

    return obey_yellow_position


def grey_filter(word_list, grey_letters):
    obey_greys = []
    for candidate in word_list:
        obey_grey_letter_test = True
        for letter in range(0, len(candidate)):
            if (candidate[letter] in grey_letters):
                obey_grey_letter_test = False
        if obey_grey_letter_test is True:
            obey_greys.append(candidate)
    return obey_greys


def big_filter(word_list, green_position, yellow_position, grey_letters):
    obey_greens = green_filter(word_list, green_position)
    obey_yellow_letters = yellow_letter_filter(obey_greens, yellow_position)
    obey_yellow_position = yellow_position_filter(obey_yellow_letters,
                                                  yellow_position)
    obey_greys = grey_filter(obey_yellow_position, grey_letters)
    obey_all = obey_greys
    return obey_all


def unused_letter_dict(word_list, guess):
    """
    Used for filtering a dictionary of words containing any letters from the
    guess (i.e. all greens, yellows, greys removed). You would use this to
    maximise your range of known letters. Especially useful on second guess.
    """
    filtered_words = []
    guess_list = list(guess)
    for word in word_list:
        obey_all = True
        for letter in range(0, len(word)):
            if word[letter] in guess_list:
                obey_all = False
        if obey_all:
            filtered_words.append(word)
    return filtered_words


def unused_yellow_dict(word_list, yellow_position, greys):
    """
Used for filtering greys, but keeping words with the yellow letters,
except where they are in the known wrong position.
    """
    obey_yellow_position = yellow_position_filter(word_list, yellow_position)
    obey_greys = grey_filter(obey_yellow_position, greys)
    obey_all = obey_greys
    return obey_all


#The below functions are not used, as they have already been combined in big filter

# def big_filter_old(word_list, green_position, yellow_position, grey_letters):
#   yellow_letters = list(filter(None, yellow_position))
#   obey_greens = []
#   for candidate in word_list:
#     obey_green_test = True
#     for letter in range(0, len(candidate)):
#       if(green_position[letter] != candidate[letter] and green_position[letter] != None):
#         obey_green_test = False
#     if obey_green_test == True:
#       obey_greens.append(candidate)
#   obey_yellow_letters = []
#   for candidate in obey_greens:
#     obeyYellowLetterTest = True
#     for letter in range(0, len(yellow_letters)):
#       if(yellow_letters[letter] not in candidate):
#         obeyYellowLetterTest = False
#     if (obeyYellowLetterTest == True):
#       obey_yellow_letters.append(candidate)
#   obey_yellow_position = []
#   for candidate in obey_yellow_letters:
#     obey_yellow_position_test = True
#     for letter in range(0, len(candidate)):
#       if(yellow_position[letter] == candidate[letter] and yellow_position[letter] != None):
#         obey_yellow_position_test = False
#     if(obey_yellow_position_test == True):
#       obey_yellow_position.append(candidate)
#   obey_greys = []
#   for candidate in obey_yellow_position:
#     obey_grey_letter_test = True
#     for letter in range(0, len(candidate)):
#       if(candidate[letter] in grey_letters):
#         obey_grey_letter_test = False
#     if(obey_grey_letter_test == True):
#       obey_greys.append(candidate)
#   obey_all = obey_greys
#   return obey_all

# def unused_yellow_dict_old(word_list, yellow_position, greys):
#   obey_yellow_position = []
#   for candidate in word_list:
#     obey_yellow_position_test = True
#     for letter in range(0, len(candidate)):
#       if(yellow_position[letter] == candidate[letter] and yellow_position[letter] != None):
#         obey_yellow_position_test = False
#     if(obey_yellow_position_test == True):
#       obey_yellow_position.append(candidate)
#   obey_greys = []
#   for candidate in obey_yellow_position:
#     obey_grey_letter_test = True
#     for letter in range(0, len(candidate)):
#       if(candidate[letter] in greys):
#         obey_grey_letter_test = False
#     if(obey_grey_letter_test == True):
#       obey_greys.append(candidate)
#   obey_greens = []
#   for candidate in obey_greys:
#     obey_green_letter_test = True
#     for letter in range(0, len(candidate)):
#       if(candidate[letter] in obey_greys):
#         obey_green_letter_test = False
#     if(obey_green_letter_test == True):
#       obey_greens.append(candidate)
#   obey_all = obey_greens
#   return obey_all
