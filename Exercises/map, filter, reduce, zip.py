from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalzing(item):
    return item.upper()


print(list(map(capitalzing, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def good_scores(item):
    return item >= 50


print(list(filter(good_scores, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def combine(list1, list2):
    x = 0
    y = 0
    new_num = 0
    while x < len(list1):
        new_num = new_num + list1[x]
        x = x + 1
    while y < len(list2):
        new_num = new_num + list2[y]
        y = y + 1
    return new_num


print(combine(scores, my_numbers))


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))

