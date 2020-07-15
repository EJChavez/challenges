# python is so powerful because it uses the power of built in modules you can import
from random import randint
# if we want to play this game in the terminal for some reason
# import sys
# random_num = randint(sys.argv[1], sys.argv[2])

random_num = randint(1, 10)
while True:
    try:
        guess = int(input('Guess a number between 1 and 10: '))
        if guess > 10 or guess <= 0:
            print('Please choose a number between 1 and 10\n')
            continue
    except:
        print('please enter an integer\n')
    else:
        if guess == random_num:
            print('you chose correctly\n')
            break
        else:
            print('you chose... poorly\n')
