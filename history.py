"""
Code that looks up the saved answers.txt file for further analysis. Used for:
- identifying a list of users
- creating an average score for each user (incomplete)
"""


def split_import(feed_file):
  """
  Split history based on "  " (a delimiter of two spaces).
  Write to a new list 'split_file'."""
  split_input = []
  for line in feed_file:
    sp_line = line.split("  ")
    split_input += sp_line
  split_input = list(filter(None, split_input)) #Remove blank items ''
  return split_input

#Selects every fifth item, which should be the usernames
  #Sets are used because they only keep unique items


def unique_users(file):
  user_name_set = set()
  for index, item in enumerate(file):
    if((index % 5) == 1):
      user_name_set.add(item)
  user_names = list(user_name_set)
  return(user_names)


def query_existing_user(name, name_set):
  return True if name in name_set else False

