import numpy as np


def grab_puzzle():
    puzzle_number = 0
    puzzle0 = [[0, 2, 0, 4, 5, 6, 7, 8, 9],
               [4, 5, 7, 0, 8, 0, 2, 3, 6],
               [6, 8, 9, 2, 3, 7, 0, 4, 0],
               [0, 0, 5, 3, 6, 2, 6, 7, 4],
               [2, 7, 4, 0, 9, 0, 6, 5, 3],
               [3, 9, 6, 5, 7, 4, 8, 0, 0],
               [0, 4, 0, 6, 1, 8, 3, 9, 7],
               [7, 6, 1, 0, 4, 0, 5, 2, 8],
               [9, 3, 8, 7, 2, 5, 0, 6, 0]]

    puzzle1 = [[0, 9, 7, 0, 0, 5, 0, 0, 1],
               [0, 4, 0, 0, 7, 0, 0, 0, 0],
               [2, 1, 3, 9, 8, 0, 0, 7, 6],
               [4, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 6, 1, 0, 5, 0, 9, 3, 0],
               [0, 0, 0, 0, 0, 8, 0, 0, 5],
               [3, 2, 0, 0, 1, 9, 4, 6, 7],
               [0, 0, 0, 0, 3, 0, 0, 8, 0],
               [1, 0, 0, 7, 0, 0, 3, 5, 0]]

    puzzle2 = [[0, 0, 0, 0, 1, 3, 0, 0, 4],
               [4, 0, 9, 0, 7, 0, 0, 0, 0],
               [7, 0, 3, 4, 0, 9, 1, 0, 0],
               [0, 0, 0, 0, 0, 8, 2, 7, 9],
               [8, 9, 0, 0, 4, 0, 0, 1, 5],
               [3, 7, 1, 9, 0, 0, 0, 0, 0],
               [0, 0, 5, 7, 0, 2, 4, 0, 3],
               [0, 0, 0, 0, 5, 0, 6, 0, 1],
               [2, 0, 0, 3, 6, 0, 0, 0, 0]]

    puzzle3 = [[2, 0, 3, 0, 0, 0, 0, 0, 8],
               [9, 0, 4, 7, 1, 8, 0, 0, 0],
               [0, 7, 0, 3, 0, 0, 0, 0, 4],
               [3, 0, 0, 0, 0, 2, 0, 0, 0],
               [5, 0, 2, 0, 4, 0, 3, 0, 9],
               [0, 0, 0, 6, 0, 0, 0, 0, 5],
               [4, 0, 0, 0, 0, 3, 0, 6, 0],
               [0, 0, 0, 2, 5, 6, 4, 0, 3],
               [6, 0, 0, 0, 0, 0, 8, 0, 7]]

    puzzle4 = [[6, 0, 2, 9, 0, 0, 8, 0, 3],
               [0, 0, 0, 0, 5, 0, 9, 0, 2],
               [1, 0, 0, 8, 0, 0, 0, 5, 0],
               [0, 0, 0, 6, 9, 0, 3, 4, 0],
               [2, 9, 0, 0, 0, 0, 0, 6, 1],
               [0, 7, 6, 0, 4, 5, 0, 0, 0],
               [0, 2, 0, 0, 0, 3, 0, 0, 5],
               [9, 0, 5, 0, 6, 0, 0, 0, 0],
               [8, 0, 3, 0, 0, 9, 1, 0, 4]]

    puzzle5 = [[0, 3, 7, 2, 9, 0, 1, 6, 0],
               [0, 0, 0, 6, 3, 8, 9, 0, 0],
               [0, 9, 6, 1, 7, 0, 0, 3, 0],
               [6, 0, 0, 9, 1, 2, 8, 7, 3],
               [9, 1, 8, 7, 5, 3, 0, 2, 0],
               [7, 2, 3, 8, 4, 6, 5, 1, 9],
               [0, 7, 0, 0, 2, 9, 3, 8, 0],
               [0, 6, 2, 3, 8, 1, 7, 9, 0],
               [3, 8, 9, 0, 6, 7, 2, 0, 1]]


    solving_loop(puzzle5)


def solving_loop(matrix):
    temp_list = []
    ci = 0
    for row in matrix:
        for column in row:
            ri = matrix.index(row)
            # print(ri, ci)
            if matrix[ri][ci] == 0:
                result = find_possible(ri, ci, matrix)
                matrix[ri][ci] = result
                temp_list.append(result)
                # print(temp_list)
                if ci == 8:
                    ci = 0
                else:
                    ci += 1
            elif ci == 8:
                ci = 0
            else:
                ci += 1
    if len(list(set(temp_list))) == 1:
        if list(set(temp_list))[0] == 0:
            print('Something went wrong')
            print(np.array(matrix))
            exit()
        else:
            solving_loop(matrix)
    elif len(list(set(temp_list))) == 0:
        print(np.array(matrix))
        exit()
    else:
        solving_loop(matrix)


def find_possible(row_i, col_i, puzzle):
    puzzle = np.array(puzzle)
    puzzle_transposed = np.transpose(puzzle)
    r1 = puzzle[0][:]
    r2 = puzzle[1][:]
    r3 = puzzle[2][:]
    r4 = puzzle[3][:]
    r5 = puzzle[4][:]
    r6 = puzzle[5][:]
    r7 = puzzle[6][:]
    r8 = puzzle[7][:]
    r9 = puzzle[8][:]
    c1 = puzzle_transposed[0][:]
    c2 = puzzle_transposed[1][:]
    c3 = puzzle_transposed[2][:]
    c4 = puzzle_transposed[3][:]
    c5 = puzzle_transposed[4][:]
    c6 = puzzle_transposed[5][:]
    c7 = puzzle_transposed[6][:]
    c8 = puzzle_transposed[7][:]
    c9 = puzzle_transposed[8][:]
    b1 = np.reshape((puzzle[0][:3], puzzle[1][:3], puzzle[2][:3]), (9,))
    b2 = np.reshape((puzzle[0][3:6], puzzle[1][3:6], puzzle[2][3:6]), (9,))
    b3 = np.reshape((puzzle[0][6:], puzzle[1][6:], puzzle[1][6:]), (9,))
    b4 = np.reshape((puzzle[3][:3], puzzle[4][:3], puzzle[5][:3]), (9,))
    b5 = np.reshape((puzzle[3][3:6], puzzle[4][3:6], puzzle[5][3:6]), (9,))
    b6 = np.reshape((puzzle[3][6:], puzzle[4][6:], puzzle[5][6:]), (9,))
    b7 = np.reshape((puzzle[6][:3], puzzle[7][:3], puzzle[8][:3]), (9,))
    b8 = np.reshape((puzzle[6][3:6], puzzle[7][3:6], puzzle[8][3:6]), (9,))
    b9 = np.reshape((puzzle[6][6:], puzzle[7][6:], puzzle[8][6:]), (9,))
    rows = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
    columns = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
    boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    r_row = rows[row_i]
    r_col = columns[col_i]
    if row_i < 3:
        if col_i < 3:
            r_box = boxes[0]
        elif col_i < 6:
            r_box = boxes[1]
        else:
            r_box = boxes[2]
    elif row_i < 6:
        if col_i < 3:
            r_box = boxes[3]
        elif col_i < 6:
            r_box = boxes[4]
        else:
            r_box = boxes[5]
    else:
        if col_i < 3:
            r_box = boxes[6]
        elif col_i < 6:
            r_box = boxes[7]
        else:
            r_box = boxes[8]
    mega = [r_row, r_col, r_box]
    mega = np.reshape(mega, (27,))
    # print(set(mega))
    test = set(mega)
    # print(row_i,col_i)
    # print(test)
    # print(len(test))
    if len(test) == 9:
        value = 45 - sum(test)
        # print(value)
        return value
    else:
        value = 0
        return value


grab_puzzle()
