import random
import sys

def generateKey(p):
    pass

    # may need modification
    # num = bin(random.randint(0,2**p - 1))
    # num = num[2:]
    # while len(num) != p:
    #     num = "0" + num
    # keys.append(num)
    # return num
# print(generateKey(4))

# for i in range(16):
def initialPermutation(s):
    bits = ""
    for char in s:
        bits += (bin(ord(char)))[0:1] + (bin(ord(char)))[2:] + " "
    return bits

    # sys.getsizeof() returns size of the string in bytes
    # n = sys.getsizeof(s)
    # 64-bit input


    # print(n)
    # return byteS
    # arrayS = bitarray.bitarray(s)
    # perm = np.random.permutation(10)
    # arrayNew = []
    # for x in len(arrayS):
    #     arrayNew[x] = (arrayS.get(perm[x]))
print(initialPermutation("abc"))
