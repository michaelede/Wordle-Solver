"""
The functions below deal with user guess inputs:
- guess_input:    prompts the user to enter their guess and  the guess score
- guess_scoring:  converts the guess into lists representing the position of green letters, yellow letters etc.
- big_filter:    filters the remaining word list for words compatible with the previous guess.
"""

def guess_input(guess_round, guesses, guess_scores):
  print('─' * 50)
  print(f"ROUND {guess_round}")
  word_length = 0
  while word_length != 5:
    input_word = input("Type your guess:  ").lower()
    word_length = len(input_word)
  score_length = 0
  while score_length != 5:
    input_score = input("Type the score:   ").lower()
    score_length = len(input_score)
  guesses.append(input_word.upper())
  guess_scores.append(input_score.upper())
  return input_word, input_score, guess_round, guesses, guess_scores


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
  green_letters = list(filter(None, green_position))
  if len(green_letters) == 5:
    five_greens = True
  else:
    five_greens = False
  yellow_letters = list(filter(None, yellow_position))
  green_yellow = green_letters + yellow_letters
  return green_position, green_letters, yellow_position, yellow_letters, grey_letters, green_yellow, five_greens


def big_filter(word_list, green_position, yellow_position, yellow_letters, grey_letters):
  obey_greens = []
  for candidate in word_list:
    obey_green_test = True
    for letter in range(0, len(candidate)):
      if(green_position[letter] != candidate[letter] and green_position[letter] != None):
        obey_green_test = False
    if obey_green_test == True:
      obey_greens.append(candidate)
  obey_yellow_letters = []
  for candidate in obey_greens:
    obeyYellowLetterTest = True
    for letter in range(0, len(yellow_letters)):
      if(yellow_letters[letter] not in candidate):
        obeyYellowLetterTest = False
    if (obeyYellowLetterTest == True):
      obey_yellow_letters.append(candidate)
  obey_yellow_position = []
  for candidate in obey_yellow_letters:
    obey_yellow_position_test = True
    for letter in range(0, len(candidate)):
      if(yellow_position[letter] == candidate[letter] and yellow_position[letter] != None):
        obey_yellow_position_test = False
    if(obey_yellow_position_test == True):
      obey_yellow_position.append(candidate)
  obey_greys = []
  for candidate in obey_yellow_position:
    obey_grey_letter_test = True
    for letter in range(0, len(candidate)):
      if(candidate[letter] in grey_letters):
        obey_grey_letter_test = False
    if(obey_grey_letter_test == True):
      obey_greys.append(candidate)
  obey_all = obey_greys
  return obey_all

def unused_letter_dict(word_list, guess):
  """
  Used for filtering a dictionary of words containing any letters from the guess (i.e. all greens, yellows, greys removed). You would use this to maximise your range of known letters. Especially useful on second guess.
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
  Used for filtering greens and greys, but keeping words with the yellow letters, except where they are in the known wrong position.
  """
  obey_yellow_position = []
  for candidate in word_list:
    obey_yellow_position_test = True
    for letter in range(0, len(candidate)):
      if(yellow_position[letter] == candidate[letter] and yellow_position[letter] != None):
        obey_yellow_position_test = False
    if(obey_yellow_position_test == True):
      obey_yellow_position.append(candidate)
  obey_greys = []
  for candidate in obey_yellow_position:
    obey_grey_letter_test = True
    for letter in range(0, len(candidate)):
      if(candidate[letter] in greys):
        obey_grey_letter_test = False
    if(obey_grey_letter_test == True):
      obey_greys.append(candidate)
  obey_greens = []
  for candidate in obey_greys:
    obey_green_letter_test = True
    for letter in range(0, len(candidate)):
      if(candidate[letter] in obey_greys):
        obey_green_letter_test = False
    if(obey_green_letter_test == True):
      obey_greens.append(candidate)  
  obey_all = obey_greens
  return obey_all

#The below functions are not used, as they have already been combined in big filter
def green_filter(word_list, green_position):
  obey_greens = []
  for candidate in word_list:
    obey_green_test = True
    for letter in range(0, len(candidate)):
      if(green_position[letter] != candidate[letter] and green_position[letter] != None):
        obey_green_test = False
    if obey_green_test == True:
      obey_greens.append(candidate)
  return obey_greens


def yellow_letter_filter(word_list, yellow_letters):
  obey_yellow_letters = []
  for candidate in word_list:
    obeyYellowLetterTest = True
    for letter in range(0, len(yellow_letters)):
      if(yellow_letters[letter] not in candidate):
        obeyYellowLetterTest = False
    if (obeyYellowLetterTest == True):
      obey_yellow_letters.append(candidate)
  return obey_yellow_letters


def yellow_position_filter(word_list, yellow_position):
  obey_yellow_position = []
  for candidate in word_list:
    obey_yellow_position_test = True
    for letter in range(0, len(candidate)):
      if(yellow_position[letter] == candidate[letter] and yellow_position[letter] != None):
        obey_yellow_position_test = False
    if(obey_yellow_position_test == True):
      obey_yellow_position.append(candidate)
  return obey_yellow_position


def grey_filter(word_list, grey_letters):
  obey_greys = []
  for candidate in word_list:
    obey_grey_letter_test = True
    for letter in range(0, len(candidate)):
      if(candidate[letter] in grey_letters):
        obey_grey_letter_test = False
    if(obey_grey_letter_test == True):
      obey_greys.append(candidate)
  return obey_greys
      
