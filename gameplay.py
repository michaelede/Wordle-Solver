# def select_engine(engine_on):
#   if not engine_on:
#     engine = None
#   else:
#     #Create Engine Menu if needed
#     engine = "engine_alpha"
#   return engine


def secret_word_input(dictionary):
    secret_word_valid = False
    while secret_word_valid == False:
        secret_word = input("Secret word: ")
        if secret_word in dictionary:
            secret_word_valid = True
        elif secret_word == "":
            secret_word = None
            secret_word_valid = True
        else:
            print("Not a valid word, please re-enter.")
    return secret_word


def random_secret_word(dictionary):
    import random
    secret_word = random.choice(dictionary)
    return secret_word


def days_since_inception():
    from datetime import date
    from datetime import datetime
    now = datetime.now()
    inception_date = date(2021, 6, 19)
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))
    today = date(year, month, day)
    days_diff = str(today - inception_date).split(" ")
    days_diff = int(days_diff[0])
    return days_diff


def today_secret_word(day_index):
    ordered_words = open("wordleOrder.txt").read().split('","')
    secret_word = ordered_words[day_index]
    return secret_word


def secret_word_menu():
    print(
        "Choose preferred option:\n  1. Play today's game\n  2. Provide Secret Word with automatic scoring\n  3. Randomly select secret word\n  4. Don't provide Secret Word & self score"
    )
    while True:
        secret_selection = input("\n                        Selection: ")
        if secret_selection == "" or secret_selection == "1":
            selection = "1"
            break
        else:
            selection = secret_selection
            break
    return selection


def robot_mode_selection(selection):
    if selection == "5":
        robot_mode = True
    else:
        robot_mode = False
    return robot_mode


def secret_word_choice(selection, dictionary):
    if selection == "" or selection == "1":
        day_diff = days_since_inception()
        secret_word = today_secret_word(day_diff)
    elif selection == "2":
        secret_word = secret_word_input(dictionary)
    elif selection == "3":
        secret_word = random_secret_word(dictionary)
    elif selection == "4":
        secret_word = None
    elif selection == "5":
        secret_word = random_secret_word(dictionary)
    return secret_word
