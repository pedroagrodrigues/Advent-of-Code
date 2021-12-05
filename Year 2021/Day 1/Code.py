def getData(path:str) -> list:
    return open(path).readlines()

data = [int(x) for x in getData("input.txt")]

# 1st question: 
print("How many measurements are larger than the previous measurement?")
answer = 0
for i in range(len(data)-1):
    if data[i] < data[i+1]:
        answer += 1
print(answer)


# 2nd question: 
print("How many sums are larger than the previous sum?")
answer = 0
for i in range(len(data)-3):
    a = 0
    b = 0

    for j in range(i, i+3):
        a += data[j]

    for j in range(i+1, i+4):
        b += data[j]

    if a < b:
        answer += 1

print(answer)