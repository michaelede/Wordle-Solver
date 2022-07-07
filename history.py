
"""
Code that looks up the saved answers.txt file for further analysis. Used for:
- identifying a list of users
- creating an average score for each user (incomplete)
"""
import pandas as pd
# from rich.console import Console
# from rich.table import Table


# history = []
# with open('answers.txt') as hist:
#     contents = hist.read().splitlines()
#     for row in contents:
#         line = row.strip().split("  ")
#         history.append(line)


# # Import to Pandas, using first row as headers
# df = pd.DataFrame(history[1:], columns=history[0],)


# convert_dict = {
#     'Datetime': str,
#     'User': 'category',
#     'Secret_word': str,
#     'Guesses': str,
#     'Guess_No': int
#     }

# # Tidy up
# df = (
#     df
#     .dropna()
#     .astype(convert_dict)
#     .assign(
#         Datetime=pd.to_datetime(df['Datetime']),
#         Date=pd.to_datetime(df['Datetime']).dt.normalize(),
#         Time=df['Datetime'].str.slice(start=-5),
#         # First_word=df['Guesses'].str[0]
#         )
#     .sort_values(by='Guess_No', ascending=True)
#     )

# df["Guesses"] = df['Guesses'].apply(eval)

# df = (
#     df
#     .assign(
#         First_guess=df['Guesses'][0]
#         )
#     )


# new_df = df[~df['User'].str.contains("Robot")]

# user_summary = (
#     df
#     [~df['User'].str.contains("Robot")]
#     .groupby('User')
#     ['User'].count()
#    .agg(
#        Attempts=({'User': ['count']}),
#        Mean=({'Guess_No': ['sum', 'mean']})
#    )
#    )


# print(new_df)
# print(user_summary)
# print(df.dtypes)


def split_import(feed_file):
    """Split history based on '  ' (a delimiter of two spaces).
    Write to a new list 'split_file'."""
    split_input = []
    for line in feed_file:
        sp_line = line.split("  ")
        split_input += sp_line
    split_input = list(filter(None, split_input))  # Remove blank items ''
    return split_input

# Selects every fifth item, which should be the usernames
# Sets are used because they only keep unique items


def unique_users(file):
    user_name_set = set()
    for index, item in enumerate(file):
        if((index % 5) == 1):
            user_name_set.add(item)
    user_names = list(user_name_set)
    return(user_names)


def query_existing_user(name, name_set):
    return True if name in name_set else False

