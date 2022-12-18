from operator import indexOf


def getData(path: str) -> list:
    return open(path).readlines()

data = getData("input.txt")

for i in range(len(data)):
    data[i] = data[i].split('\n')[0]

# Casting strings to int
data = [int(value) if value != '' else value for value in data]


# Counting elements of array
calories = [[]]
[calories.append([]) if y == '' else calories[-1].append(y) for y in data]
calories = [sum(x) for x in calories]

# Result part 1:
print("Result of part 1: ", max(calories))

# --- Part 2 ---

sumThreeElves = 0

for _ in range(3):
    sumThreeElves += max(calories)
    calories.remove(max(calories))

# Result part 2:
print("Result of part 2: ", sumThreeElves)