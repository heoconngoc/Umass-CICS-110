# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase (word, guess_lst):
    result=''
    for char in word:
      if (not char.isalpha()) or char in guess_lst:
        result += char
      else:
        result += '_'
    print(result)

# print_revealed_phrase("PUMPKIN PIE", ['N', 'P', 'S', 'E'])
# # >>> P_ _P_ _N P_E
# print_revealed_phrase("EUREKA! IT'S 5:00PM.", [])
# # >>> _ _ _ _ _ _! _ _'_ 5:00_ _.
# print_revealed_phrase("EUREKA! IT'S 5:00PM.", ['E', 'P', 'S', 'T'])
# # >>> E _ _ E _ _! _ T'S 5:00P _.

def get_letter(guess_lst):
  while True:  
    guess = input('Please enter a letter: ').upper()
    if not guess.isalpha() or len(guess) != 1:
      print(f'"{guess}" is not a letter!')    
      continue
    if guess in guess_lst:
      print(f'"{guess}" has already been guessed!')
      continue
    break
  guess_lst.append(guess)
  return guess

# get_letter(['A', 'B', 'C'])
# # >>> Please enter a letter: a
# # >>> "A" has already been guessed!
# # >>> Please enter a letter: 9
# # >>> "9" is not a letter!
# # >>> Please enter a letter: d

def won(target, guess_lst):
  for char in target:
    if char.isalpha():
      if not char in guess_lst:
        return False
  return True
# print(won("PUMPKIN PIE", ['N', 'P', 'S', 'E']))
# # >>> False
# print(won("PUMPKIN PIE", ['N', 'P', 'S', 'E', 'U', 'M', 'K', 'I']))
# # >>> True
# print(won("EUREKA! IT'S 5:00PM.", ['E','U','R','K','A','I','T','S','P','M']))
# # >>> True

def play_game():
  phrase = make_phrase()
  misses = 0
  guess_lst = []
  print('*** Welcome to Hangman ***')
  print_gallows(misses)

  while True:
    print_revealed_phrase(phrase, guess_lst)
    print(f'Letters guessed: {sorted(guess_lst)}')
    guess = get_letter(guess_lst)

    if not guess in phrase:
      misses += 1
      print_gallows(misses)
      if misses == 6:
        print('Game Over!')
        print(f'Solution was: {phrase}')
        break
    else:
      if won(phrase,guess_lst):
        print_revealed_phrase(phrase,guess_lst)
        print('Congratulations!')
        break
play_game()