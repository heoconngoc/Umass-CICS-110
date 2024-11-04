# Author: Quoc Dat Pham
# Email: quocdatpham@umass.edu
#Spire ID: 34740949

def count_words(words):
    my_dict = {}
    for word in words: 
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

# words = ('he', 'saw', 'a', 'saw', 'saw', 'a', 'saw')
# print(count_words(words))

def average_prices(prices):
    total_dict = {}
    count_dict = {}
    for price in prices:
        item, value = price
        if item in total_dict:
            total_dict[item] += value
            count_dict[item] += 1
        else:
            total_dict[item] = value
            count_dict[item] = 1

    average_dict = {}
    for item in total_dict:
         average_dict[item]= total_dict[item] / count_dict[item]
    return average_dict

# prices = (('a', 1.0), ('c', 4.2), ('b', 3.9), ('a', 1.2), ('d', 10.4), ('b', 4.3), ('b', 3.8))
# print(average_prices(prices))
# Output → {'a': 1.1, 'c': 4.2, 'b': 4.0, 'd': 10.4}

