
#Defining the variables that are used in the functions
inputWord = None     #The user's guess
inputScore = None    #The score for the guess
guesses = []         #A record of the guesses
greenPosition = []   #Identifying the position of each green letter
greenLetters = []    #A list of the green letters
yellowPosition = []  #Identifying the position of each yellow letter
yellowLetters = []   #A list of the yellow letters
greyLetters = []     #A list of the grey letters
obeyGreens = []      #A list of the words that obey the Green letters
obeyYellowPosition = [] #A list of the words that obey the Yellow Positions
obeyYellowLetters = [] #A list of the words that obey the Yellow exclusion
obeyGreys = []       #A list of the words that don't have grey letters
greenYellow = []     #A list of the confirmed letters
validSolutions = validWords #The working list of allowable words through each round
wordCount = None     #Count of the valid words
continueValue = True #A boolean for stopping the While loop

def takeInput():
  global inputWord, inputScore, greenLetters, greenPosition, yellowLetters, yellowPosition, greyLetters, guesses, guessRound
  guessRound += 1
  print('─' * 50)
  print(f"ROUND {guessRound}")
  inputWord = input("Type your guess:  ").lower()  #Converts responses to lower case
  inputScore = input("Type the score:   ").lower() #Converts scores to lower case
  guesses.append(inputWord.upper())
  for letter in range(0, len(inputScore)):
    if inputScore[letter] == "g":
      greenPosition.append(inputWord[letter])
    elif inputScore[letter] == ".":
      greenPosition.append(inputWord[letter])
    else:
        greenPosition.append(None)
  for letter in range(0, len(inputScore)):
    if inputScore[letter] == "y":
      yellowPosition.append(inputWord[letter])
    if inputScore[letter] == ",":
      yellowPosition.append(inputWord[letter])
    else:
      yellowPosition.append(None)
  for letter in range(0, len(inputScore)):
    if inputScore[letter] == "-":
      greyLetters.append(inputWord[letter])
    elif inputScore[letter] == "/":
      greyLetters.append(inputWord[letter])
  greenLetters = list(filter(None, greenPosition))
  yellowLetters = list(filter(None, yellowPosition))
  greenYellow = greenLetters + yellowLetters
  return inputWord, inputScore, guesses, guessRound, greenLetters, yellowLetters, yellowPosition, greyLetters, greenYellow

def greenFilter():
  for candidate in validSolutions:
    global obeyGreens
    obeyGreenTest = True
    for letter in range(0, len(candidate)):
      if(greenPosition[letter] != candidate[letter] and greenPosition[letter] != None):
        obeyGreenTest = False
    if obeyGreenTest == True:
      obeyGreens.append(candidate)

def yellowLetterFilter():
  for candidate in obeyGreens:
    global obeyYellowLetters
    obeyYellowLetterTest = True
    for letter in range(0, len(yellowLetters)):
      if(yellowLetters[letter] not in candidate):
        obeyYellowLetterTest = False
    if (obeyYellowLetterTest == True):
      obeyYellowLetters.append(candidate)

def yellowPositionFilter():
  for candidate in obeyYellowLetters:
    global obeyYellowPosition
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

def showWords():
  print(f"There are {wordCount} eligible words.")
  revealWords = input("Would you like to see them? (y/n/#): ")
  validSolutionsUpper = []
  for i in range(len(validSolutions)):
    validSolutionsUpper.append(validSolutions[i].upper())
  if(revealWords=="y"):
    my_len = len(validSolutionsUpper)
    my_len = (my_len-my_len%5)+5
    my_range = my_len//5
    print("")
    fin_list = [validSolutionsUpper[i*5:i*5+5] for i in range(my_range)]
    for item in fin_list:
      print("  ", "    ".join(item))
  if(revealWords.isnumeric()):
    s = slice(0,int(revealWords))
    sWords = (validSolutionsUpper[s])
    my_len = len(sWords)
    my_len = (my_len-my_len%5)+5
    my_range = my_len//5
    print("")
    fin_list = [sWords[i*5:i*5+5] for i in range(my_range)]
    for item in fin_list:
      print("  ", "    ".join(item))

def continuation():
  global continueValue
  continueValue=True
  if(inputScore=="ggggg"):
    continueValue=False
  elif(inputScore=="....."):
    continueValue=False

def conclusion():
  print('─' * 50)
  joinGuesses = ", ".join(guesses)
  print(f"Congratulations, you completed the game in {guessRound} attempts.")
  print(f"Your guesses were: {joinGuesses}\n")
  global secretWord
  secretWord = (validSolutions[0]).upper()
  print(f"The secret word was {secretWord}.")

def bigFilter():
  global validSolutions
  global obeyGreys
  global obeyGreens
  global obeyYellowLetters
  global obeyYellowPosition
  global wordCount
  global greenPosition
  global yellowPosition
  global greenYellow
  takeInput()
  obeyGreens = []
  greenFilter()
  obeyYellowLetters = []
  yellowLetterFilter()
  obeyYellowPosition = []
  yellowPositionFilter()
  obeyGreys = []
  greyFilter()
  validSolutions = []
  validSolutions = obeyGreys
  wordCount = len(validSolutions)
  obeyGreens = []
  obeyYellowPosition = []
  greenPosition = []
  yellowPosition = []
  obeyYellowLetters = []
  obeyGreys = []
  if(wordCount == 1):
    conclusion()
  else:
    showWords()

while continueValue == True:
  bigFilter()
  continuation()

saveValue = input("Save? (y/n): ")
if (saveValue != "n"):
  saveString = f"\n{dt_string}  {user}  {secretWord}  {guessRound}  {guesses}  "
  with open('answers.txt', 'a') as f:
    f.write(saveString)
  print("Done.")
print("Thank you for playing.")