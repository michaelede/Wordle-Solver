

# Main Loop
def main_loop(guess_round, guesses, all_words, yellow_dict,
              guess_scores, print_sequence, grey_letters,
              valid_dictionary, continue_value, secret_word):
    import solver, problem, Engines, modules
    while continue_value:
        guess_round += 1
        print('─' * 50)
        print(f"ROUND {guess_round}\n")

        input_word = solver.guess_input()
        print_word = " ".join(list(input_word.upper()))
        if secret_word is None:
            input_score = solver.score_input()
        else:
            input_score = problem.scoring(input_word, secret_word)
        print_score = solver.score_colour(input_score)
        print_sequence = solver.printable_sequence(print_word,
                                                   print_score, print_sequence)
        solver.print_results(print_word, print_score)

        guesses.append(input_word.upper())
        guess_scores.append(input_score.upper())
        input_scoring = solver.guess_scoring(input_word,
                                             input_score, grey_letters)
        green_position = input_scoring[0]
        green_letters = list(filter(None, green_position))
        yellow_position = input_scoring[1]
        yellow_letters = list(filter(None, yellow_position))
        grey_letters = input_scoring[2]
        green_yellow = green_letters + yellow_letters
        five_greens = solver.five_greens(green_position)

        valid_dictionary = solver.big_filter(valid_dictionary, green_position,
                                             yellow_position, grey_letters)

        if len(valid_dictionary) == 1 and five_greens is False:
            print(f"\nThere is only one valid word:     {valid_dictionary[0]}")
        else:
            Engines.alpha_report(input_word, valid_dictionary, all_words,
                                 yellow_dict, green_position, yellow_position,
                                 grey_letters, green_yellow)
        continue_value = modules.continuation(continue_value,
                                              input_score, guess_round)
    return guess_round, print_sequence


# Robot Loop
def robot_loop(guess_round, guesses, all_words, yellow_dict,
               guess_scores, print_sequence, grey_letters, valid_dictionary,
               continue_value, secret_word, top_choice):
    import solver, problem, Engines, modules
    while continue_value:
        guess_round += 1
        input_word = top_choice
        print_word = " ".join(list(input_word.upper()))
        input_score = problem.scoring(input_word, secret_word)
        print_score = solver.score_colour(input_score)
        print_sequence = solver.printable_sequence(print_word, print_score,
                                                   print_sequence)

        guesses.append(input_word.upper())
        guess_scores.append(input_score.upper())
        input_scoring = solver.guess_scoring(input_word, input_score,
                                             grey_letters)
        green_position = input_scoring[0]
        green_letters = list(filter(None, green_position))
        yellow_position = input_scoring[1]
        yellow_letters = list(filter(None, yellow_position))
        grey_letters = input_scoring[2]
        green_yellow = green_letters + yellow_letters
        five_greens = solver.five_greens(green_position)

        valid_dictionary = solver.big_filter(valid_dictionary, green_position,
                                             yellow_position, grey_letters)

        top_choice = Engines.alpha_solve(input_word, valid_dictionary,
                                         all_words, yellow_dict, green_position,
                                         yellow_position, grey_letters, green_yellow)
        continue_value = modules.continuation(continue_value, input_score, guess_round)
    return guess_round, print_sequence
