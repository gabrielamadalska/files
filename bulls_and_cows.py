import random
number = []

def MakeNum():
    for i in range(4):
        x = random.randrange(0,9)
        number.append(x)
    print(number)

MakeNum()