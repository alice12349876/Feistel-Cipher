import random

def generateKey(p):
    num = bin(random.randint(0,2^p - 1))
    num = num[2:]
    while len(num) != p:
        num = "0" + num
print(generateKey(4))
