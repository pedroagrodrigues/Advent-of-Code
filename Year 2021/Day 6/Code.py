def getData(path: str) -> list:
    return open(path).readlines()


data = [int(x) for x in getData("input.txt")[0].split(",")]

# 1st question:
print("How many lanternfish would there be after 80 days?")



def getTotalLanternfish(num: list) -> int:

    # Dictionary for counting days
    days = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
    }
    for i in data:
        days[i] += 1

    while num:
        temp = days[0]
        for i in range(len(days)-1):
            days[i] = days[i+1]

        days[6] += temp
        days[8] = temp 



    
        num -= 1
    return(sum(days.values()))


print(getTotalLanternfish(80))

# 2nd question:
print("How many lanternfish would there be after 256 days?")
print(getTotalLanternfish(256))
