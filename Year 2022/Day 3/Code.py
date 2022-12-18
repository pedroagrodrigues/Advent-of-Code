def getData(path: str) -> list:
    return open(path).read()


data = getData("input.txt").split('\n')

part1 = [[x[:len(x)//2], x[len(x)//2:]] for x in data]


total = 0

itemValue = {}


def calcValue(char): return ord(char) - 38 if char.isupper() else ord(item) - 96


for items in part1:
    checked = []
    for item in items[0]:
        if item in items[1] and item not in checked:
            total += calcValue(item)
            checked.append(item)

print(f"(Part 1) the totale is: {total}")


# ---- Day 2 ----
total = 0

for i in range(0, len(data), 3):
    checked = []
    for item in data[i]:
        if item in data[i+1] and item in data[i+2] and item not in checked:
            total += calcValue(item)
            checked.append(item)

print(f"(Part 2) the totale is: {total}")
