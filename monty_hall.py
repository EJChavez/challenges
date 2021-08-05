import random

def monty_hall():
    wins_o = 0
    wins_n = 0
    loops = 0
    while loops < 1000:
        doors = ['Door 1', 'Door 2', 'Door 3']
        winning_door = doors[random.randint(0,2)]
        my_door = doors[random.randint(0,2)]
        wins_o += optimal(doors,winning_door,my_door)
        wins_n += unoptimal(winning_door,my_door)
        loops += 1
    print(wins_o,wins_n)


def optimal(doors,winning_door,my_door):
    doors.remove(my_door)
    if winning_door in doors:
        return 1
    else:
        return 0

def unoptimal(winning_door,my_door):
    if winning_door == my_door:
        return 1
    else:
        return 0


monty_hall()
