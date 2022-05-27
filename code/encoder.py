import random
import sys
import codecs

shiftTable = []
for i in range(16):
    if (i in [0, 1, 8, 15]):
        shiftTable.append(1)
    else:
        shiftTable.append(2)

paritDrop = []
for i in range(16):
    #
    pass

# print(shiftTable)
key = bytes(sys.argv[1], encoding='utf-8')
# print(key)
hexify = codecs.getencoder('hex')
print(hexify(key))

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
        bits += bin(ord(char))
    # 64-bit input: loop through the bits, divie into groups of 64

    # perform permutation. Need to think of ways of recovering this as part of decryption?
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
# print((initialPermutation(key)))
# print(len(initialPermutation(key)))
