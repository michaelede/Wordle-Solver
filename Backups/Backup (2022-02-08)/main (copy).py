"""
This is the main code, pulling together functions from the other modules.
Future ideas:
- Historic data for each person
- Solver mode - where you provide the solution amd can look at different pathways to the solution.
- Show colour box representation of guess & score.
- Suggest words that aren't on the answer list or compatible with previous answers but which will more speedily get to the answer.
"""
import problem
problem


#Dates
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M")

#Initialisation
import history
import solver
import modules
import frequency
guess_round = 0
guesses = []
guess_scores = []
grey_letters = []
continue_value = True
valid_words = open("wordleList.txt").read().split() #Get Data
allowed_words = open("wordleAllowed.txt").read().split()
all_words = valid_words + allowed_words
dictionary = valid_words
yellow_dict = all_words
#Get the names of historic users
raw_history = open("answers.txt").read().splitlines()  #Split into a list based on the line break
history_file = history.split_import(raw_history) #Split history by delimiter
user_names = history.unique_users(history_file) #Get unique user names from history file

#letter_freq = frequency.frequecy_analysis(dictionary, [], 26) #Unhash line to see letter frequencies of unfiltered words

#Introduction
print("Wordle Solver")
print("A tool to help solve the daily Wordle puzzle at: https://www.powerlanguage.co.uk/wordle/\n")
print(dt_string)
print("Valid Answers: ", len(valid_words)) 
user = input("\nWhat is your name? ")
legit_user = history.query_existing_user(user, user_names)
if legit_user:
  print(f"Welcome back!\n")
else:
  print(f"Hi {user}, you seem to be new here. Use the same name in the future for saving historic scores.\n")

print("For Scoring:\n  Grey:    - or /\n  Green:   G or .\n  Yellow:  Y or ,")
print('Recommended first guesses: ORATE, or ALERT followed by SONIC')

#Main Loop
while continue_value:
  guess_round += 1
  inputs = solver.guess_input(guess_round, guesses, guess_scores)
  input_scoring = solver.guess_scoring(inputs[0], inputs[1], grey_letters)
  dictionary = solver.big_filter(dictionary, input_scoring[0], input_scoring[2], input_scoring[3], input_scoring[4])
  untried_letter_dict = solver.unused_letter_dict(all_words, inputs[0])
  unused_yellow_dict = solver.unused_yellow_dict(yellow_dict, input_scoring[2], input_scoring[4])
  if len(dictionary) > 1:
    letter_freq = frequency.frequecy_analysis(dictionary, input_scoring[5], 10)
    if len(dictionary) >= 10:
      print("\nTo maximise available information, choose from the below which exclude previously guessed letters but are optimised for letter frequency in the remaining valid words:")
      frequency.recommended_words(untried_letter_dict, letter_freq, 5)
    elif len(dictionary) >= 3:
      print("\nTo maximise available information, choose from the below which exclude previously guessed letters apart from yellows but are optimised for letter frequency in the remaining valid words:")
      frequency.recommended_words(unused_yellow_dict, letter_freq, 5)      
    print("\nIf making a guess these words - which have equal probability - will maximise the information you gain if you are wrong. The highest scored words are:")
    frequency.recommended_words(dictionary, letter_freq, 10)
    print("")
    modules.show_words(dictionary)
  elif len(dictionary) == 1 and input_scoring[6] == False:
    print(f"\nThere is only one valid word:     {dictionary[0]}")
  continue_value = modules.continuation(continue_value, inputs[1])


#Termination
secret_word = modules.conclusion(guesses)
saveValue = input("Save? (y/n): ")
if (saveValue != "n"):
  saveString = f"\n{dt_string}  {user}  {secret_word}  {guess_round}  {guesses}  "
  with open('answers.txt', 'a') as f:
    f.write(saveString)
  print("Done.")
print("Thank you for playing.")