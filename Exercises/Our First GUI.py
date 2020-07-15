def Ethan_First_Attempt():
    # Exercise!
    # Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]
    #print(picture)
    x = 0
    y = 0
    picture2 = picture.copy()
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
    x = 0
    y = 1
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
    x = 0
    y = 2
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
    x = 0
    y = 3
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
    x = 0
    y = 4
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
    x = 0
    y = 5
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
    x = 0
    y = 6
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1

    x = 0
    while x < 6:
        print(picture[x])
        x = x + 1
#Ethan_First_Attempt()

def ethan_cleaned_attempt():
    # Exercise!
    # Display the image below to the right hand side where the 0 is going to be ' '
    # and the 1 is going to be '*'. This will reveal an image!
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]
    # print(picture)
    x = 0 # x is down
    y = 0 # y is across
    picture2 = picture.copy()
    while x < 6:
        if picture[x][y] == 0:
            picture2[x][y] = ' '
        elif picture[x][y] == 1:
            picture2[x][y] = '*'
        x = x + 1
        if x == 6:
            x = 0
            y = y + 1
            if y == 7:
                break
    while x < 6:
        print(picture2[x])
        x = x + 1
ethan_cleaned_attempt()

def ethan_while():
    # supercleaned
    # Exercise!
    # Display the image below to the right hand side where the 0 is going to be ' '
    # and the 1 is going to be '*'. This will reveal an image!
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]
    # print(picture)
    down = 0  # x is down
    across = 0  # y is across
    while down < 6:
        if picture[down][across] == 1:
            print('*', end='')
        elif picture[down][across] == 0:
            print('')
        while across < 7:
            if picture[down][across] == 1:
                print('*', end='')
            elif picture[down][across] == 0:
                print('')
            across = across + 1
            if across == 7:
                across = 0
                break
        down = down + 1


def howitsdone():
    # Exercise!
    # Display the image below to the right hand side where the 0 is going to be ' '
    # and the 1 is going to be '*'. This will reveal an image!
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    for row in picture:
        for item in row:
            if item == 1:
                print('$', end='')
            else:
                print(' ', end='')
        print('')


def instructor_solution():
    # Exercise!
    # Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    for row in picture:
        for column in row:
            if (column == 1):
                print('*', end="")
            else:
                print(' ', end="")
        print('')
instructor_solution()