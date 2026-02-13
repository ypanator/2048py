from curses import wrapper
from drawBoard import drawBoard
from handleInput import handleInput
from calcBoard import calcBoard
from constants import *

def main(stdscr):
    curChar = None
    board = [[None] * 4 for _ in range(4)]
    board[0][0] = 2048
    board[2][3] = 2
    board[0][2] = 2

    drawBoard(stdscr, board)
    while curChar != q:
        direction = handleInput(curChar)

        if direction == error:
            pass
        else:
            calcBoard(board, direction)
            drawBoard(stdscr, board)

        curChar = stdscr.getch()

wrapper(main)
# https://docs.python.org/3/howto/curses.html