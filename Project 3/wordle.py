# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def get_guess():
    return input("What word is this?: ").upper()

def print_word(str):
    print(' '.join(str))

def exact_match_compare(guess, sol):
    mes = ''
    for i in range (0,5):
        if guess[i] == sol[i]:
            mes += '🟢'
        else:
            mes += '🔴'
    return mes

def one_turn(sol):
    guess = get_guess()
    print_word(guess)
    print(exact_match_compare(guess, sol))
    if exact_match_compare(guess, sol) == '🟢🟢🟢🟢🟢':
        print("Congratulations!")
        exit()

import random
def make_solution():
    a = "WHICH", "THEIR", "THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"
    return random.choice(a)


soln = make_solution()
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
one_turn(soln)
print(f"Word was \"{soln}\", better luck next time.")