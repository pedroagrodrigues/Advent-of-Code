def getData(path: str) -> list:
    return open(path).readlines()


data = [
    [[int(element) for element in list] for list in sublist]
    for sublist in [
        [z.split(",") for z in y] for y in [x.split("->") for x in getData("input.txt")]
    ]
]

# 1st question:
print("At how many points do at least two lines overlap?")

points = {}


def addToPoits(x: int, y: int):
    lst = str([x, y])
    if lst in points:
        points[lst] += 1
    else:
        points[lst] = 1

def sumRepetitions(book: dict) -> int:
    return sum(book[i] >= 2 for i in book)


    
for i in data:
    x1, y1 = iter(i[0])
    x2, y2 = iter(i[1])
    addToPoits(x1, y1)

    if x1 != x2:
        while x1 <= x2:
            x1 += 1
            addToPoits(x1, y1)

    if x1 != x2:
        while x1 >= x2:
            x1 -= 1
            addToPoits(x1, y1)
    
    if y1 != y2:
        while y1 <= y2:
            y1 += 1
            addToPoits(x1, y1)
    if y1 != y2:
        while y1 >= y2:
            y1 -= 1
            addToPoits(x1, y1)



print(sumRepetitions(points))