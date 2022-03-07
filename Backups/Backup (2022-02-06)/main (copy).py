# word_list = ["shark", "pants", "smart", "plate", "beech", "coins"]
# green_yellow = ["a", "e"]

# output = frequency.partial_words(word_list, green_yellow)
# print(output)
# freq = frequency.frequency(output)
# print(freq)
# frequency.best_letters(freq, 10)
# scored_words = frequency.scored_words(output, freq)
# print(scored_words)
# frequency.best_words(word_list, scored_words, 5)
#scored_words, 5)

import frequency


# frequency.frequecy_analysis(word_list, word_list, green_yellow, 5, 10)


#Dates
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M")


#Initialisation
import history
import solver
import modules
guess_round = 0
guesses = []
guess_scores = []
grey_letters = []
continue_value = True
valid_words = open("wordleList.txt").read().split() #Get Data
allowed_words = open("wordleAllowed.txt").read().split()
all_words = valid_words + allowed_words
dictionary = valid_words

#Get the names of historic users
raw_history = open("answers.txt").read().splitlines()  #Split into a list based on the line break
history_file = history.split_import(raw_history) #Split history by delimiter
user_names = history.unique_users(history_file) #Get unique user names from history file

#Introduction
print("Wordle Solver")
print(dt_string)
print("Valid Answers: ", len(valid_words)) 
user = input("\nWhat is your name? ")
legit_user = history.query_existing_user(user, user_names)
if legit_user:
  print(f"Welcome back!\n")
else:
  print(f"Hi {user}, you seem to be new here. Use the same name in the future for saving historic scores.\n")

print("For Scoring:\n  Grey:    - or /\n  Green:   G or .\n  Yellow:  Y or ,")
print('Recommended first guesses: ALERT and SONIC')

#Main Loop
while continue_value:
  guess_round += 1
  inputs = solver.guess_input(guess_round, guesses, guess_scores)
  print(inputs[3])
  input_scoring = solver.guess_scoring(inputs[0], inputs[1], grey_letters)
  dictionary = solver.big_filter(dictionary, input_scoring[0], input_scoring[2], input_scoring[3], input_scoring[4])
  if(len(dictionary)>1):
    frequency.frequecy_analysis(dictionary, dictionary, input_scoring[5], 5, 10)
    modules.show_words(dictionary)
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