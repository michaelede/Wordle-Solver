print("Wordle Solver")

validWords = open("wordleList.txt").read().split()
print("Valid Answers: ", len(validWords))
print('First five words: ', *validWords[0:5])
print("For Scoring: - = Grey, G = Green, Y = Yellow")
print('Recommended first guesses: ALERT and SONIC')

inputWord = None
inputScore = None
guessRound = 1
greenPosition = []
greenLetters = []
yellowPosition = []
yellowLetters = []
greyLetters = []
obeyGreens = []
obeyYellowPosition = []
obeyYellowLetters = []
obeyGreys = []
validSolutions = validWords


def takeInput():
  global inputWord
  global inputScore
  global greenLetters
  global yellowLetters
  inputWord = input("Type your guess:  ").lower()
  inputScore = input("Type the score:   ").lower()
  for letter in range(0, len(inputScore)):
    if inputScore[letter] == "g":
        greenPosition.append(inputWord[letter])
    else:
        greenPosition.append(None)
  for letter in range(0, len(inputScore)):
    if inputScore[letter] == "y":
        yellowPosition.append(inputWord[letter])
    else:
        yellowPosition.append(None)
  for letter in range(0, len(inputScore)):
    if inputScore[letter] == "-":
      greyLetters.append(inputWord[letter])
  greenLetters = list(filter(None, greenPosition))
  yellowLetters = list(filter(None, yellowPosition))

takeInput()

def greenFilter():
  for candidate in validSolutions:
    obeyGreenTest = True
    for letter in range(0, len(candidate)):
      if(greenPosition[letter] != candidate[letter] and greenPosition[letter] != None):
        obeyGreenTest = False
    if obeyGreenTest == True:
      obeyGreens.append(candidate)

def yellowLetterFilter():
  for candidate in obeyGreens:
    obeyYellowLetterTest = True
    for letter in range(0, len(yellowLetters)):
      if(yellowLetters[letter] not in candidate):
        obeyYellowLetterTest = False
    if (obeyYellowLetterTest == True):
      obeyYellowLetters.append(candidate)

def yellowPositionFilter():
  for candidate in obeyYellowLetters:
    obeyYellowPositionTest = True
    for letter in range(0, len(candidate)):
      if(yellowPosition[letter] == candidate[letter] and yellowPosition[letter] != None):
        obeyYellowPositionTest = False
    if(obeyYellowPositionTest == True):
      obeyYellowPosition.append(candidate)

def greyFilter():
  for candidate in obeyYellowPosition:
    obeyGreyLetterTest = True
    for letter in range(0, len(candidate)):
      if(candidate[letter] in greyLetters):
        obeyGreyLetterTest = False
    if(obeyGreyLetterTest == True):
      obeyGreys.append(candidate)

def bigFilter():
  greenFilter()
  print(len(obeyGreens))
  #print(obeyGreens)
  yellowLetterFilter()
  print(len(obeyYellowLetters))
  yellowPositionFilter()
  print(len(obeyYellowPosition))
  greyFilter()
  print(len(obeyGreys))
  validSolutions = obeyGreys
  obeyGreens = []
  obeyYellowLetters = []
  obeyYellowPosition = []
  obeyGreys = []

bigFilter()
print(obeyGreys)
print(validSolutions)
