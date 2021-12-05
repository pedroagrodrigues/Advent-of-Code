def getData(path:str) -> list:
    return open(path).readlines()

data = [[y[0], int(y[1])] for y in [x.split(' ') for x in getData("input.txt")]]

# 1st question: 
print("What do you get if you multiply your final horizontal position by your final depth?")

# coordinates:
x = 0 # horizontal
y = 0 # vertical

for i, j in data:
    if i == "forward":
        x += j
    if i == "up":
        y -= j
    if i == "down":
        y += j

print(x*y)

# 2nd question:
print("What do you get if you multiply your final horizontal position by your final depth?")# coordinates:

x = 0 # horizontal
y = 0 # vertical
z = 0 # aim

for i, j in data:
    if i == "forward":
        x += j
        y += z*j
    if i == "up":
        z -= j
    if i == "down":
        z += j

print(x*y)