def ethan_attempt():
    # exercise: check for duplicates in list:
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    test_list = some_list.copy
    item = 0
    myset = set()
    other_list = []
    while item < len(some_list):
        # print(some_list[item])
        if some_list[item] not in myset:
            myset.add(some_list[item])
        elif some_list[item] in myset:
            other_list.append(some_list[item])
        item = item + 1
    print(other_list)
ethan_attempt()

#WHAT HE TOLD ME I CANT USE SETS
def ethan_nosets():
    # exercise: check for duplicates in list:
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    test_list = []
    duplicates = []
    item = 0
    while item < len(some_list):
        if some_list[item] not in test_list:
            test_list.append(some_list[item])
        else:
            duplicates.append(some_list[item])
        item = item + 1
    print(duplicates)
ethan_nosets()

def ethaniffloopsinstructersolution():
    # exercise: check for duplicates in list:
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            duplicates.append(value)
            for thingy in duplicates:
                if duplicates.count(thingy) > 1:
                    duplicates.remove(thingy)

    print(duplicates)


def instructer_solution():
    # exercise: check for duplicates in list:
    some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)


    print(duplicates)