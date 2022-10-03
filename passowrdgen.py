# A simple python password genrator
# Author: Mawuena

import secrets, string

class color:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    CWHITE = '\33[37m'
    
    
    
def passwdGen():

    pwd_length = 9

    letters = string.ascii_letters

    digits = string.digits

    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    generated_random_password = ""

    for i in range(pwd_length):
        generated_random_password += ''.join(secrets.choice(alphabet))

    print(color.GREEN + "[!] " + color.CWHITE + "Generated password = " + generated_random_password)

    return generated_random_password

print(passwdGen())