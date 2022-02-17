# Secure Password Check

## How to run:

- On *Windows*, enter `python check.py` into the command line.
- On *Linux*, enter `python3 check.py` into the command line.
- Once it is running, enter a password;
- The program will return `True` if secure, and `False` if insecure.
  - For example, `password!3712821JKL` will return `True`.


## Password Requirements:

##### To be secure, a password must:
- Be a 5 word password separated by spaces; where
- Each word must contain 3 or more characters; and
- Only alphabetic characters `A-Z` or `a-z` (Latin alphabet) are present.



##### Alternatively, it must:
- Be 12 or more characters long;
- Contain uppercase characters `A-Z` (Latin alphabet);
- Contain lowercase characters `a-z` (Latin alphabet);
- Contain Digits `0-9`;
- Contain special characters (`!`, `$`, `#`, `%`, etc.); and
- There can not be 3 or more consecutive characters (e.g. 'aaa').


  These types of passwords are difficult to remember and are becoming less ideal in many scenarios as the landscape of password cracking changes; ideal with a password manager.


---

Created on January 10, 2020.
