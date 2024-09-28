# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

import string
import random

# 25% of the characters should be uppercase letters
# 25% should be lowercase letters
# 25% should be numbers
# The rest of the characters should be special characters

def password_generator(length: int):
    up = int(length/4)
    low = int(length/4)
    num = int(length/4)
    spe = length - up - low - num

    uppercase = random.choices(string.ascii_uppercase, k = up)
    lowercase = random.choices(string.ascii_lowercase, k = low)
    digit = random.choices(string.digits, k = num)
    special = random.choices(string.punctuation, k = spe)

    result = ''.join(uppercase + lowercase + digit + special)

    return result

