"""
This page is to build the decoder algorithms. Different engines can be created with different levels of agression etc.
"""
import solver
import frequency
import modules

def comments(selection):
  maximise = "\nTo maximise available information, choose from the below which exclude previously guessed letters but are optimised for letter frequency in the remaining valid words:"
  maximise_yellows = "\nTo maximise available information, choose from the below which exclude previously guessed letters apart from yellows but are optimised for letter frequency in the remaining valid words:"
  guess = "\nIf making a guess these words - which have equal probability - will maximise the information you gain if you are wrong. The highest scored words are:"
  if selection == "maximise":
    return maximise
  elif selection == "maximise_yellows":
    return maximise_yellows
  elif selection == "guess":
    return guess


def alpha_solve(input_word, valid_dictionary, all_words, yellow_dict, green_position, yellow_position, grey_letters, green_yellow):
  untried_letter_dict = solver.unused_letter_dict(all_words, input_word)
  unused_yellow_dict = solver.unused_yellow_dict(yellow_dict, yellow_position, grey_letters)
  
  if len(valid_dictionary) > 1:
    letter_freq = frequency.frequecy_analysis_robot(valid_dictionary, green_yellow, 10)
    if len(valid_dictionary) >= 10:
      top_choice = frequency.recommended_words(untried_letter_dict, letter_freq, 5)
    elif len(valid_dictionary) >= 3:
      top_choice = frequency.recommended_words(unused_yellow_dict, letter_freq, 5)
    elif len(valid_dictionary) == 2:
      top_choice = valid_dictionary[0]
  elif len(valid_dictionary) == 1:
    top_choice = valid_dictionary[0]
  return top_choice



def alpha_report(input_word, valid_dictionary, all_words, yellow_dict, green_position, yellow_position, grey_letters, green_yellow):
  untried_letter_dict = solver.unused_letter_dict(all_words, input_word)
  unused_yellow_dict = solver.unused_yellow_dict(yellow_dict, yellow_position, grey_letters)
  
  if len(valid_dictionary) > 1:
    letter_freq = frequency.frequecy_analysis(valid_dictionary, green_yellow, 10)
    if len(valid_dictionary) >= 10:
      print(comments("maximise"))
      frequency.recommended_words_report(untried_letter_dict, letter_freq, 5)

    elif len(valid_dictionary) >= 3:
      print(comments("maximise_yellows"))
      frequency.recommended_words_report(unused_yellow_dict, letter_freq, 5)        
    print(comments("guess"))

    frequency.recommended_words_report(valid_dictionary, letter_freq, 10)
    print("")
    modules.show_words(valid_dictionary)