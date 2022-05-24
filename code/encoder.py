import random

def generateKey(p):
    return bin(random.randint(0,2^p - 1))
print(generateKey(4))
