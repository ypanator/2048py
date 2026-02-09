from curses import wrapper
import curses

q = ord("q")
w = ord("w")
d = ord("d")
s = ord("s")
a = ord("a")
up = 1
right = 2
down = 3
left = 4
error = 5
vert = 0
hori = 1

def main(stdscr):
    curChar = None
    board = [[None] * 4 for _ in range(4)]
    board[0][0] = 2
    board[2][3] = 3
    board[0][2] = 10

    while curChar != q:
        direction = handleChar(curChar)

        if direction == error:
            pass
        else:
            calcBoard(board, direction)
            drawBoard(stdscr, board)

        curChar = stdscr.getch()

def handleChar(char):
    if char == w: return up
    if char == d: return right
    if char == s: return down
    if char == a: return left
    return error

# oh god
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

def drawBoard(scr, board):
    # grid is 9x9
    # curses cords are (y, x)
    # window top left is (0, 0)

    y, x = 4, curses.COLS // 2 - 4
    scr.addstr(y, x, "+-+-+-+-+")
    y += 1
    for row in board:
        num1 = row[0] if row[0] is not None else " "
        num2 = row[1] if row[1] is not None else " "
        num3 = row[2] if row[2] is not None else " "
        num4 = row[3] if row[3] is not None else " "
        scr.addstr(y, x, 
            f"|{num1}|{num2}|{num3}|{num4}|")
        y += 1
        scr.addstr(y, x, "+-+-+-+-+")
    scr.refresh()

wrapper(main)
# https://docs.python.org/3/howto/curses.html