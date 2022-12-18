import itertools

def getData(path: str) -> list:
    return open(path).read()

data = getData("input.txt").split('\n')



''' 
First column is the opponent:
    A -> Rock
    B -> Paper
    C -> Scissors

Points:
    0 -> Losing
    3 -> Drawing
    6 -> Wining

    Points per play:
        Rock -> 1
        Paper -> 2 
        Scissors -> 3

    Total: 
        Points played + outcome

Assumption:
    Y -> Paper
    X -> Rock
    Z -> Scissors

'''

# Spliting data into array of arrays:
data = [ x.split(' ') for x in data ]

# Converting data to play according with the following dictionary
plays = {
    "Rock" : ['A' , 'X'],
    "Paper" : ['B', 'Y'],
    "Scissors" : ['C', 'Z']
}

for play, i in itertools.product(data, range(2)):
    play[i] = "Rock" if play[i] in plays["Rock"] else "Paper" if play[i] in plays["Paper"] else "Scissors"

# Counting points for plays

score = 0

for i in data:
    if i[1] == "Rock":
        score += 1
    elif i[1] == "Paper":
        score += 2
    elif i[1] == "Scissors":
        score += 3


# Counting game outcomes

for i in data:
    if i[0] == i[1]:
        score += 3
    elif i[0] == "Rock" and i[1] == "Paper" or i[0] == "Scissors" and i[1] == "Rock" or i[0] == "Paper" and i[1] == "Scissors":
        score += 6

print("(Part 1) The total score is: ", score)



# ---------------------- Part 2 ----------------------

'''
New strategy
    Y = Draw
    X = Lose
    Z = Win
'''

# Rebuilding data
data = [x.split(' ') for x in getData("input.txt").split('\n')]

# Converting data to play according with the following dictionary

plays = {
    "Rock" : 'A',
    "Paper" : 'B',
    "Scissors" : 'C'
}


for play in data:
    if play[1] == 'Y':  # Draw
        play[1] = play[0]

    elif play[1] == 'X': # Lose
        if play[0] == 'A':
            play[1] = 'C'
        elif play[0] == 'B':
            play [1] = 'A'
        else: 
            play[1] = 'B'

    elif play[0] == 'A': # Win
        play[1] = 'B'
    elif play[0] == 'B':
        play [1] = 'C'
    else: 
        play[1] = 'A'

# Renaming data
for play, i in itertools.product(data, range(2)):
    play[i] = "Rock" if play[i] in plays["Rock"] else "Paper" if play[i] in plays["Paper"] else "Scissors"

# Counting points for plays

score = 0

for i in data:
    if i[1] == "Rock":
        score += 1
    elif i[1] == "Paper":
        score += 2
    elif i[1] == "Scissors":
        score += 3


# Counting game outcomes

for i in data:
    if i[0] == i[1]:
        score += 3
    elif i[0] == "Rock" and i[1] == "Paper" or i[0] == "Scissors" and i[1] == "Rock" or i[0] == "Paper" and i[1] == "Scissors":
        score += 6

print("(Part 2) The total score is: ", score)



