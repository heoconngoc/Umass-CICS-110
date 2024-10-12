# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')

def get_protein(order):
    if order[3] == 'chicken':
        return 2.5
    elif order[3] == 'steak':
        return 3.5
    elif order[3] == 'barbacoa':
        return 3.5
    elif order[3] == 'carnitas':
        return 3.0
    elif order[3] == 'veggies':
        return 2.5
    else:
        return 0

# print(get_protein(order1))
# # >>> 2.5 
# print(get_protein(order2))
# # >>> 3.0

def get_rice(order):
    if order[4] == 'white':
        return 2.5
    elif order[4] == 'brown':
        return 3.5
    else:
        return 0

# print(get_rice(order1))
# # >>> 2.5 
# print(get_rice(order2))
# # >>> 3.5

def get_beans(order):
    if order[5] == 'black':
        return 2.5
    elif order[5] == 'pinto':
        return 2.5
    else:
        return 0

# print(get_beans(order1))
# # >>> 2.5 
# print(get_beans(order2))
# # >>> 2.5

def get_burrito(order):
    if order[6] == True:
        return 2.0
    else:
        return 0

# print(get_burrito(order1))
# # >>> 0
# print(get_burrito(order2))
# # >>> 2.0

def get_toppings(order):
    sum = 0
    for i in range (7, len(order)):
        price = check(i, order)
        sum += price
    return sum

def check(i, order):
    if(order[3] == 'veggies' and order[i] == 'guacamole'):
        return 0
    if(order[3] == 'veggies' and order[i] == 'fajita veggies'):
        return 0

    if order[i] == "guacamole":
        return 2.75
    elif order[i] == "tomato salsa":
        return 2.5
    elif order[i] == "chili corn salsa":
        return 1.75
    elif order[i] == "tomatillo green chili salsa":
        return 2.0
    elif order[i] == "cheese":
        return 2.0
    elif order[i] == "sour cream":
        return 2.5
    elif order[i] == "queso blanco":
        return 2.75
    elif order[i] == "fajita veggies":
        return 2.5
    else:
        return 0

# print(get_toppings(order1))
# # >>> 9.75
# print(get_toppings(order2))
# # >>> 12.25

def apply_discount(order, total):
    if order[2] == 'MAGIC':
        return total*95/100
    elif order[2] == 'SUNDAYFUNDAY':
        return total*90/100
    elif order[2] == 'FLAT3':
        return total - 3
    else:
        return total

# print(apply_discount(order1, 17.25))
# # >>> 14.25
# print(apply_discount(order2, 23.25))
# # >>> 22.0875

def approximate_time(order):
    if order[1] == 'amherst':
        return 15
    elif order[1] == 'north amherst':
        return 15
    elif order[1] == 'south amherst':
        return 15
    elif order[1] == 'hadley':
        return 15
    elif order[1] == 'northampton':
        return 30
    elif order[1] == 'south hadley':
        return 30
    elif order[1] == 'belchertown':
        return 30
    elif order[1] == 'sunderland':
        return 30
    elif order[1] == 'holyoke':
        return 45
    elif order[1] == 'greenfield':
        return 45
    elif order[1] == 'deerfield':
        return 45
    else:
        return 45

# print(approximate_time(order1))
# # >>> 45
# print(approximate_time(order2))
# # >>> 45
def get_total(order):
    return get_protein(order) + get_rice(order) + get_beans(order) + get_burrito(order) + get_toppings(order)
def burito(order):
    if order[6] == True:
        return "Yes"
    else:
        return "No"    

def generate_invoice(order):
    print(f'Welcome to Chipotle Mexican Grill Hadley, {order[0]}.')
    print('Your invoice is displayed below:')
    print(f'Protein: {order[3]} - ${get_protein(order)}')
    print(f'Rice: {order[4]} rice - ${get_rice(order)}')
    print(f'Beans: {order[5]} beans - ${get_beans(order)}')
    print(f'Burrito: {burito(order)} - ${get_burrito(order)}')
    print(f'Toppings: {', '.join(order[7:])} - ${get_toppings(order)}')
    print(f'Subtotal: ${ get_total(order)}')
    print(f'Discount Code: {order[2]}')
    print(f'Total: ${apply_discount(order, get_total(order))}')
    print(f'You Save: ${get_total(order) - apply_discount(order, get_total(order))}')
    print(f'Your order will be ready in {approximate_time(order)} minutes.')
    print('Enjoy your meal and have a good day!')

# generate_invoice(order2)