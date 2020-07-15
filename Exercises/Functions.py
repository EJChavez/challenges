def highest_even(*args):
    mylist.sort()
    mylist.reverse()
    total = 0
    while total < len(mylist):
        if mylist[total] % 2 == 0:
            print(f'{mylist[total]} is the highest even')
            break
        else:
            total = total + 1
mylist = [10,2,3,4,8,11,100,192034821,28194657561,389563425,3289154317,21574321853,21685936270]
highest_even(mylist)

def highest_even_instructer(li):
    evens = []
    for item in li:
        if item % 2 == 0
            evens.append(item)
    return max(evens)
print(highest_even_instructer([10,2,3,4,8,11]))