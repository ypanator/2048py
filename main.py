from curses import wrapper
from drawBoard import drawBoard
from handleInput import handleInput
from calcBoard import calcBoard, placeNewNum
from constants import *
from scanBoard import scanBoard

def main(stdscr):
    curChar = None
    board = [[None] * 4 for _ in range(4)]
    maxNum = placeNewNum(board, [(0, 0)])

    drawBoard(stdscr, board)
    while curChar != q:
        data = scanBoard(board)
        direction = handleInput(curChar)

        if direction == error:
            pass
        else:
            calcBoard(board, direction)
            placeNewNum(board, data.emptySpots)
            drawBoard(stdscr, board)

        curChar = stdscr.getch()

wrapper(main)
# https://docs.python.org/3/howto/curses.html``