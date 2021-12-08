def getData(path: str) -> list:
    return open(path).readlines()


data = [int(x) for x in getData("input.txt")[0].split(",")]

# 1st question:
print("How much fuel must they spend to align to that position? (1st)")


def sumFuel(position: int) -> int:
    fuel = 0
    for i in data:
        if i > position:
            fuel += i - position
        if i < position:
            fuel += position - i
    return fuel


def bestSpot() -> int:
    best = float("inf")
    for i in data:
        temp = sumFuel(i)
        best = min(best, temp)
    return best


print(bestSpot())

# 2nd question:
print("How much fuel must they spend to align to that position? (2nd)")

def sumFuel2(position: int) -> int:
    fuel = 0
    for i in data:
        distance = 0
        if i > position:
            distance = i - position
        if i < position:
            distance = position - i

        for j in range(distance):
            fuel += j+1

    return fuel

def bestSpot2() -> int:
    best = float("inf")
    done = []
    limits = max(data)
    for i in range(limits):
        if i not in done:
            temp = sumFuel2(i)
            best = min(best, temp)
            done.append(i)
    return best

print(bestSpot2())