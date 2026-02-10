from constants import *

def calcBoard(board, direction):
    vel, axis, xrange, yrange = None, None, None, None
    if direction == up:
        axis = vert
        xrange = (0, 4, 1)
        yrange = (0, 4, 1)
        vel = 1
    if direction == right:
        axis = hori
        xrange = (3, -1, -1)
        yrange = (0, 4, 1)
        vel = -1
    if direction == down:
        axis = vert
        xrange = (0, 4, 1)
        yrange = (3, -1, -1)
        vel = -1
    if direction == left:
        axis = hori
        xrange = (0, 4, 1)
        yrange = (0, 4, 1)
        vel = 1

    for x in range(*xrange):
        for y in range(*yrange):

            if board[y][x] is None:
                continue
            num = board[y][x]
            placed = False
            revVel = 1 if vel == -1 else -1
            x2 = x + revVel if axis == hori else x
            y2 = y + revVel if axis == vert else y
            while 4 > x2 >= 0 and 4 > y2 >= 0:
                if board[y2][x2] == num:
                    board[y2][x2] = 2 * num
                    placed = True
                    break
                elif board[y2][x2] is not None:
                    x2 -= revVel if axis == hori else 0
                    y2 -= revVel if axis == vert else 0
                    board[y2][x2] = num
                    placed = True
                    break
                x2 += revVel if axis == hori else 0
                y2 += revVel if axis == vert else 0
            if not placed:
                x2 -= revVel if axis == hori else 0
                y2 -= revVel if axis == vert else 0
                board[y2][x2] = num
            if y != y2 or x != x2:
                board[y][x] = None
    
    # TODO: implement placing new num on empty spot