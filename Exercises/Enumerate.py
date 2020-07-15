#enumerate similar to range

#enumerate gives in index number for the Iterable object (sets, lists, tuples, strings, dicts)
# for index,char in enumerate({1,2,3,4,5}):
#     print(index,char)

for i,num in enumerate(list(range(0,100,2))):
    if num == 50:
        print(i,num) #'i was correct here'

for index, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {index}') #how he did it.

