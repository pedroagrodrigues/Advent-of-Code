def getData(path: str) -> list:
    return open(path).readlines()


data = [x for x in getData("input.txt")]

# 1st question:
print("In the output values, how many times do digits 1, 4, 7, or 8 appear?")

outputLens = [2, 3, 4, 7]
total = 0
for i in data:
    for j in i.split("|")[1].split():
        if len(j) in outputLens:
            total += 1

print(total)

# 2nd question:
print("What do you get if you add up all of the output values?")

numbers = {
    'acedgfb': 8,
    'cdfbe': 5,
    'gcdfa': 2,
    'fbcad': 3,
    'dab': 7,
    'cefabd': 9,
    'cdfgeb': 6,
    'eafb': 4,
    'cagedb': 0,
    'ab': 1
}

total = 0
for i in data:
    line = ''
    for j in i.split("|")[1].split():
        print(j in numbers)
    # total += eval(line)


print(total)
