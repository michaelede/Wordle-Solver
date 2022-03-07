"""
Helper modules ancillary to the main functions/algorithms:
- show_words: prints the remaining pool of words. A value can be provided to limit to n.
- continuation: a boolean flag to trigger then end of the program when a correct guess has been made.
- conclusion: final code
"""
def clear_row():
    print ("\033[A                                  \033[A")


def show_words(dictionary):
    print(f"There are {len(dictionary)} eligible words.")
    revealWords = input("Would you like to see them? (y/n/#): ")
    valid_solutions_lower = []
    for i in range(len(dictionary)):
        valid_solutions_lower.append(dictionary[i].lower())
    if(revealWords=="y"):
        my_len = len(valid_solutions_lower)
        my_len = (my_len-my_len%5)+5
        my_range = my_len//5
        print("")
        fin_list = [valid_solutions_lower[i*5:i*5+5] for i in range(my_range)]
        for item in fin_list:
            print("  ", "    ".join(item))
    if(revealWords.isnumeric()):
        s = slice(0,int(revealWords))
        sWords = (valid_solutions_lower[s])
        my_len = len(sWords)
        my_len = (my_len-my_len%5)+5
        my_range = my_len//5
        print("")
        fin_list = [sWords[i*5:i*5+5] for i in range(my_range)]
        for item in fin_list:
            print("  ", "    ".join(item))


def continuation(continue_value, input_score, round_no):
    continue_value=True
    if input_score=="ggggg" or input_score == ".....":
        continue_value=False
    elif round_no == 6:
        continue_value = False
    return continue_value


def conclusion(print_sequence):
    print('─' * 50)
    join_guesses = "\n             ".join(print_sequence)
    length = int(len(print_sequence) / 2)
    print(f"Congratulations, you completed the game in {length} attempts.")
    print(f"Your guesses were:\n")
    print(f"             {join_guesses}\n")
    secret_word_string = (print_sequence[-2]).upper()
    secret_word = []
    for i in secret_word_string:
        if i != " ":
            secret_word.append(i)
    secret_word = "".join(secret_word)
    print(f"The secret word was {secret_word}.")
    return secret_word


def commentary(text_selection):
    print_maximise = print("\nTo maximise available information, choose from the below which exclude previously guessed letters but are optimised for letter frequency in the remaining valid words:")
    print_maximise2 = print("\nTo maximise available information, choose from the below which exclude previously guessed letters apart from yellows but are optimised for letter frequency in the remaining valid words:")
    print_guess = print("\nIf making a guess these words - which have equal probability - will maximise the information you gain if you are wrong. The highest scored words are:")
    if text_selection == "maximise":
        return print_maximise
    elif text_selection == "maximise2":
        return print_maximise2
    elif text_selection == "guess":
        return print_guess


def append_string(file, string):
    with open(file, 'a') as f:
        f.write(string)


def termination(dt_string, user, secret_word, guess_round, guesses, print_sequence):
    secret_word = conclusion(print_sequence)
    saveValue = input("Save? (y/n): ")
    if (saveValue != "n"):
        saveString = f"\n{dt_string}  {user}  {secret_word}  {guess_round}  {guesses}  "
        append_string('answers.txt', saveString)
        print("Done.")
    print("Thank you for playing.")


def robot_termination(dt_string, user, secret_word, guess_round, guesses, print_sequence):
    secret_word = conclusion(print_sequence)
    saveString = f"\n{dt_string}  'Robot'  {secret_word}  {guess_round}  {guesses}  "
    append_string('robot_results.txt', saveString)

