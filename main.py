

#Dates
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M")


#Initialisation
import history, big_loop, modules, gameplay
guess_round = 0
secret_mode = False
guesses = []
guess_scores = []
grey_letters = []
print_sequence = []
continue_value = True
top_choice = "Alert"


with open("wordleList.txt") as f:
    valid_words = f.read().split() #Get Data

with open("wordleAllowed.txt") as f:
    allowed_words = f.read().split()

all_words = valid_words + allowed_words
valid_dictionary = valid_words
yellow_dict = all_words

#Get the names of historic users
with open("answers.txt") as f:
    raw_history = f.read().splitlines()  #Split into a list based on the line break
history_file = history.split_import(raw_history) #Split history by delimiter
user_names = history.unique_users(history_file) #Get unique user names from history file

#letter_freq = frequency.frequecy_analysis(valid_dictionary, [], 26) #Unhash line to see letter frequencies of unfiltered words

#Introduction
print("Wordle Solver")
print("A tool to help solve the daily Wordle puzzle at: https://www.powerlanguage.co.uk/wordle/\n")
print(dt_string)
user = input("\nWhat is your name? ")
legit_user = history.query_existing_user(user, user_names)
if legit_user:
    modules.clear_row()
    print(f"Hi {user}, welcome back!\n")
else:
    modules.clear_row()
    print(f"Hi {user}, you seem to be new here.\nUse the same name in the future for saving historic scores.\n")

gameplay_selection = gameplay.secret_word_menu()
secret_word = gameplay.secret_word_choice(gameplay_selection, valid_words)
robot_mode = gameplay.robot_mode_selection(gameplay_selection)


#secret_word = gameplay.secret_word_input(all_words)
if secret_word == None:
    print("\nFor Scoring:\n  Grey:    - or /\n  Green:   G or .\n  Yellow:  Y or ,")


#Termination
iterations = 5

if robot_mode:
    for i in range(0, iterations):
        print(f"Iteration {i} of 1")
        print_sequence = []
        guesses = []
        main_outputs = big_loop.robot_loop(guess_round, guesses, all_words, yellow_dict, guess_scores, print_sequence, grey_letters, valid_dictionary, continue_value, secret_word, top_choice)
        guess_round = main_outputs[0]
        print_sequence = main_outputs[1]  
        modules.robot_termination(dt_string, user, secret_word, guess_round, guesses, print_sequence)

else:
    main_outputs = big_loop.main_loop(guess_round, guesses, all_words, yellow_dict, guess_scores, print_sequence, grey_letters, valid_dictionary, continue_value, secret_word)
    guess_round = main_outputs[0]
    print_sequence = main_outputs[1]
    modules.termination(dt_string, user, secret_word, guess_round, guesses, print_sequence)

