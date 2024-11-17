# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def print_stars_to_file(n):
  with open(f"stars_{n}.txt", "w") as file:
    for i in range(1, n + 1):
      spaces = " " * (n - i)
      stars = "*" * (2 * i - 1)
      file.write(spaces + stars + "\n")

def calc_avg_from_file():
  total = 0
  num = 0
  with open("grades.txt","r") as file:
    text = file.read()
    grades = text.split("\n")
    for grade in grades:
      num += 1
      total += float(grade)
    return total/num



