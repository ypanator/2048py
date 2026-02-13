class Data:
    def __init__(self):
        self.emptySpots = []
        self.maxNum = 0

def scanBoard(board):
    data = Data()

    for x in range(4):
        for y in range(4):
            if board[y][x] is None:
                data.emptySpots.append((y, x))
            else:
                data.maxNum = max(data.maxNum, board[y][x])

    return data