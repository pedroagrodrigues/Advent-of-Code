def getData(path:str) -> list:
    return open(path).readlines()

data = [list(x.split()[0]) for x in getData("input.txt")]

# 1st question: 
print("What is the power consumption of the submarine?")
gama = []
epsilon = []
for i in range(len(data[0])):
    zeros = 0
    ones = 0
    for line in data:
        if line[i] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gama.append('0')
        epsilon.append('1')
    else:
        gama.append('1')
        epsilon.append('0')

gama = eval('0b' + ''.join(gama))
epsilon = eval('0b'+''.join(epsilon))

print(gama*epsilon)

# 2nd question:
print("What is the life support rating of the submarine?")



def o2(lst:list) -> int:
    index = 0
    while len(lst) > 1:
        zeros = 0
        ones = 0
        for line in lst:
            if line[index] == '0':
                zeros += 1
            else:
                ones += 1
        lst = [x for x in lst if x[index] == '0'] if zeros > ones else [x for x in lst if x[index] == '1']
        index += 1


    return eval('0b'+''.join(lst[0]))

def co2(lst:list) -> int:
    index = 0
    while len(lst) > 1:
        zeros = 0
        ones = 0
        for line in lst:
            if line[index] == '0':
                zeros += 1
            else:
                ones += 1
        lst = [x for x in lst if x[index] == '1'] if ones < zeros else [x for x in lst if x[index] == '0']
        index += 1

    return eval('0b'+''.join(lst[0]))

print(o2(data)*co2(data))