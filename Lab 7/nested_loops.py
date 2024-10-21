def get_names(first_names, last_names):
    full_names=[]
    for fname in first_names:
        for lname in last_names:
            name = fname + ' ' + lname
            full_names.append(name)
    return full_names


# Lateness = 0 → 100% credit (no penalty)
# Lateness = 1 → 90% credit
# Lateness = 2 → 75% credit
# Lateness = 3 → 50% credit
# Lateness ≥ 4 → 0% credit

def average_scores(scores):
    result = []
    for student in scores:
        total = 0
        num = 0
        for score in student:
            num += 1
            if score[1] == 0:
                total += score[0]
            elif score[1] == 1:
                total += score[0]* 0.9
            elif score[1] == 2:
                total += score[0]* 0.75
            elif score[1] == 3:
                total += score[0]* 0.5
            else:
                total += 0
        result.append(total / num)
    return result 

# print(average_scores([[(90, 0), (80, 1), (70, 2), (60, 3), (50, 4)], [(100, 10), (90, 0), (80, 0), (90, 0)], [(0, 0), (20, 0), (40, 1), (100, 0), (100, 0), (100, 0)]]))