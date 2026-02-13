from constants import *

def handleInput(char):
    if char == ord("w"): return up
    if char == ord("d"): return right
    if char == ord("s"): return down
    if char == ord("a"): return left
    if char == ord("q"): return quit
    if char == ord("e"): return restart
    return error