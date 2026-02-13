from curses import wrapper
from drawBoard import drawBoard
from handleInput import handleInput
from calcBoard import calcBoard, placeNewNum
from constants import *
from scanBoard import scanBoard
from drawEnd import drawEnd

def main(stdscr):
    state = play
    action = None
    board = [[None] * 4 for _ in range(4)]
    maxNum = placeNewNum(board, [(0, 0)])

    drawBoard(stdscr, board)
    action = handleInput(stdscr.getch())
    while action == error:
        action = handleInput(stdscr.getch())

    def resetBoard(stdscr):
        nonlocal state, board, maxNum
        state = play
        board = [[None] * 4 for _ in range(4)]
        maxNum = placeNewNum(board, [(0, 0)])
        stdscr.clear()
        drawBoard(stdscr, board)

    while action != quit:
        data = scanBoard(board)
        maxNum = data.maxNum
        if data.emptySpots == []:
            state = end
            stdscr.clear()
        
        if action == restart:
            resetBoard(stdscr)

        elif state == end:
            drawEnd(stdscr, maxNum)
            while action != quit and action != restart:
                action = handleInput(stdscr.getch())
            if action == quit: break
            resetBoard(stdscr)

        elif state == play:
            calcBoard(board, action)
            placeNewNum(board, data.emptySpots)
            drawBoard(stdscr, board)

        else:
            raise ValueError("Invalid state")

        action = handleInput(stdscr.getch())
        while action == error:
            action = handleInput(stdscr.getch())

    
wrapper(main)
# https://docs.python.org/3/howto/curses.html``