from constants import *

def handleInput(char):
    if char == w: return up
    if char == d: return right
    if char == s: return down
    if char == a: return left
    if char == q: return quit
    if char == e: return restart
    return error