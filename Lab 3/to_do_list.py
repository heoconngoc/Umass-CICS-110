# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----
def add_task(to_do_list, description):
  to_do_list.append(description)
  x = len(to_do_list)
  return(f"Task successfully added. {x} tasks remaining.")

def delete_task(to_do_list, description):
  to_do_list.remove(description)
  x = len(to_do_list)
  return(f"Task successfully deleted. {x} tasks remaining.")

def move_task(to_do_list, from_index, to_index):
  x = to_do_list[from_index]
  to_do_list.remove(x)
  to_do_list.insert(to_index,x)
  return(f"Task '{x}' successfully moved to index {to_index}")
# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# # Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))

# # Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
print(delete_task(to_do_list, 'zybook reading'))
print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')
