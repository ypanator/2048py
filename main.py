from curses import wrapper

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

def main(stdscr):
    curChar = None
    board = [[None] * 4 for _ in range(4)]

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

def calcBoard(board, direction):
    axis, xrange, yrange = None, None, None
    if direction == up:
        pass
    if direction == right:
        pass
    if direction == down:
        pass
    if direction == left:
        pass

    # currently, up only
    for x in range(4):
        for y in range(4):

            if board[y][x] is None:
                continue
            num = board[y][x]
            placed = False
            for i in range(y-1, -1, -1):
                if board[i][x] == num:
                    board[i][x] = 2 * num
                    placed = True
                    break
                elif board[i][x] is not None:
                    board[i-1][x] = num
                    placed = True
                    break
            if not placed:
                board[i][x] = num
            board[y][x] = None

def drawBoard(scr, board):
    # https://docs.python.org/3/howto/curses.html
    pass

wrapper(main)