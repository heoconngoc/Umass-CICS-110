# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def stop (traffic_light, pedestrian):
    if(traffic_light == 'Red' or pedestrian == True):
        return True
    else:
        return False
# print(stop('Red', False))
# print(stop('Green', False))

def move_forward(traffic_light, pedestrian):
    if(pedestrian == False):
        if(traffic_light == 'Green' or traffic_light == 'Yellow'):
            return True
        else:
            return False
    else:
        return False
# print(move_forward('Green', False))
# print(move_forward('Red', False))
# print(move_forward('Yellow', False))
# print(move_forward('Yellow', True))

def turn_left(traffic_light, pedestrian,cars_opposite):
    if(traffic_light == 'Green'  and pedestrian == False and cars_opposite == False):
        return True
    return False
# print(turn_left('Green', False, True))
# print(turn_left('Green', False, False))
# print(turn_left('Red', False, False))