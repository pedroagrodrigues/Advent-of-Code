def getData(path: str) -> list:
    return open(path).readlines()


data = [x.split() for x in getData("input.txt")]

# 1st question:
print("What will your final score be if you choose that board?")

# First get the drawn numbers
drawn = [int(x) for x in data.pop(0)[0].split(",")]

# data = data[1:] # removing the first empty list

boards = []

while data:
    if data[0] == []:
        boards.append([])
        data.pop(0)
    else:
        boards[-1].append([int(x) for x in data.pop(0)])


def check(board: list) -> bool:
    debug = True
    for line in board:
        if all(x == -1 for x in line):
            return True
        if -1 in line:
            index = line.index(-1)
            if all(y[index] == -1 for y in [x for x in board]): return True
    return False


def getWinnerBoard() -> list:
    while len(drawn) > 0 and len(boards) > 0:
        currentNumber = drawn.pop(0)
        for board in boards:
            for line in board:
                if currentNumber in line:
                    line[line.index(currentNumber)] = -1  # Assuming all drawns are integer and >= 0
                    if [number for line in board for number in line].count(-1) >= 5 and check(board):
                        boards.pop(boards.index(board))
                        return currentNumber, [[x for x in line if x != -1] for line in board]
    # for i in drawn:
    #     for board in boards:
    #         for line in board:
    #             if i in line:
    #                 line[line.index(i)] = -1  # Assuming all drawns are integer and >= 0
    #                 if [number for line in board for number in line].count(-1) >= 5 and check(board):

    #                     return i, [[x for x in line if x != -1] for line in board]
                        


lastDrawn, winner = getWinnerBoard()
winnerSum = sum(sum(x) for x in winner)

print(lastDrawn * winnerSum)

# 2nd question: 
print("Once it wins, what would its final score be?")



def getLoserBoard() -> list:
    while len(drawn) > 0 and len(boards) > 0:
        currentNumber = drawn.pop(0)
        for board in boards:
            for line in board:
                if currentNumber in line:
                    line[line.index(currentNumber)] = -1  # Assuming all drawns are integer and >= 0

        for board in boards:
            for line in board:
                if [number for line in board for number in line].count(-1) >= 5 and check(board):
                    lastBoard = boards.pop(boards.index(board))
                    break
    
    return currentNumber, [[x for x in line if x != -1] for line in lastBoard]


loserNumberCall, loserBoard = getLoserBoard()


print(sum(sum(x) for x in loserBoard) * loserNumberCall)
