import re #Python regular expression ~ used for string searching
from itertools import groupby

def consec(password):
  return re.search(r'(.)\1\1', password) is None

def check_password(password):
  meets_requirements = False
  # min length is 12
  # at least 1 digit
  # at least 1 uppper and 1 lower char
  # at least 1 special char

  words = [ i for i in password.split() ]

  if len(words) == 1:
    r_p1 = re.compile('^(?=\S{12,}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')

    s = re.search(r_p1, password)
    if s and consec(password):
      meets_requirements = True

  else:
    if len(words) < 5:
      return False
    for word in words:
      if not (len(word) > 2 and word.isalpha()):
        return False

    meets_requirements = True

  return meets_requirements


password = input()
print(check_password(password))
