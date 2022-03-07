"""
Helper modules ancillary to the main functions/algorithms:
- show_words: prints the remaining pool of words. A value can be provided to limit to n.
- continuation: a boolean flag to trigger then end of the program when a correct guess has been made.
- conclusion: final code
"""


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


def continuation(continue_value, input_score):
  continue_value=True
  if(input_score=="ggggg"):
    continue_value=False
  elif(input_score=="....."):
    continue_value=False
  return continue_value


def conclusion(guesses):
  print('─' * 50)
  join_guesses = ", ".join(guesses)
  print(f"Congratulations, you completed the game in {len(guesses)} attempts.")
  print(f"Your guesses were: {join_guesses}\n")
  secret_word = (guesses[-1]).upper()
  print(f"The secret word was {secret_word}.")
  return secret_word

