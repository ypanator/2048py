from constants import *

def handleInput(char):
    if char == w: return up
    if char == d: return right
    if char == s: return down
    if char == a: return left
    return error