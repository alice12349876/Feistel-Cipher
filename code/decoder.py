import random
import sys
import codecs

def hexToBits(str):
    # print(str)
    stringBit = ""
    for i in range(len(str)):
        hexVal = str[i]
        if hexVal == '0':
            stringBit += "0000"
        elif hexVal == '1':
            stringBit += "0001"
        elif hexVal == '2':
            stringBit += "0010"
        elif hexVal == '3':
            stringBit += "0011"
        elif hexVal == '4':
            stringBit += "0100"
        elif hexVal == '5':
            stringBit += "0101"
        elif hexVal == '6':
            stringBit += "0110"
        elif hexVal == '7':
            stringBit += "0111"
        elif hexVal == '8':
            stringBit += "1000"
        elif hexVal == '9':
            stringBit += "1001"
        elif hexVal == 'A' or 'a':
            stringBit += "1010"
        elif hexVal == 'B' or 'b':
            stringBit += "1011"
        elif hexVal == 'C' or 'c':
            stringBit += "1100"
        elif hexVal == 'D' or 'd':
            stringBit += "1101"
        elif hexVal == 'E' or 'e':
            stringBit += "1110"
        elif hexVal == 'F' or 'f':
            stringBit += "1111"
    return stringBit

def bitsToHex(str):
    finString = ""
    for i in range(int(len(str)/4)):
        bitVal = str[i*4:i*4+4]
        # print(bitVal)
        if bitVal == "0000":
            finString += "0"
        elif bitVal == "0001":
            finString += "1"
        elif bitVal == "0010":
            finString += "2"
        elif bitVal == "0011":
            finString += "3"
        elif bitVal == "0100":
            finString += "4"
        elif bitVal == "0101":
            finString += "5"
        elif bitVal == "0110":
            finString += "6"
        elif bitVal == "0111":
            finString += "7"
        elif bitVal == "1000":
            finString += "8"
        elif bitVal == "1001":
            finString += "9"
        elif bitVal == "1010":
            finString += "A"
        elif bitVal == "1011":
            finString += "B"
        elif bitVal == "1100":
            finString += "C"
        elif bitVal == "1101":
            finString += "D"
        elif bitVal == "1110":
            finString += "E"
        elif bitVal == "1111":
            finString += "F"
    return finString

def initialPermutation(stringBit):
    initialArray = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    newString = ""
    for i in initialArray:
        newString = newString + stringBit[i-1]
    return newString

#64 bit -> 64 bit
def roundCalculation(stringBit, curRound, keyBit):
    a = stringBit[32:] + xor(ffunction(stringBit[32:], curRound, keyBit), stringBit[0:32])
    return a

def ffunction(right, curRound, keyBit):
    a = expansion(right)
    a = xor(a, keyBit)
    a = sbox(a)
    a = straightPerm(a)
    return a

def xor(str1, str2):
    s = ""
    # print(len(str1))
    # print(len(str2))
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            s += "0"
        else:
            s += "1"
    return s

def expansion(right):
    expanArray = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 31, 31, 32, 1]
    newString = ""
    for i in expanArray:
        newString = newString + right[i-1]
    return newString

def sbox(a):
    # a is a 48 bit input
    # each S box corresponds to one group of 8-bit input
    sboxArray =  [[[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], [0,15,7,4,14,2,13,10,3,6,12,11,9,5,3,8], [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0], [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
    [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10], [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15], [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
    [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8], [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1], [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7], [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
    [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15], [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9], [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4], [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
    [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9], [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6], [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14], [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
    [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11], [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8], [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], [4,3,2,12,9,5,15,10,11,14,1,7,10,0,8,13]],
    [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1], [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6], [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
    [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7], [1,15,13,8,10,3,7,4,12,5,6,11,10,14,9,2], [7,11,4,1,9,12,14,2,0,6,10,10,15,3,5,8], [2,1,14,7,4,10,8,13,15,12,9,9,3,5,6,11]]
    ]
    newString = ""
    row = 0
    column = 0
    for i in range(1,9):
        # binary to int for row and column index
        row = int(a[6*i-6] + a[6*i-1], 2)
        column = int(a[6*i-5] + a[6*i-4] + a[6*i-3] + a[6*i-2], 2)
        # 4 bit output
        # print(row)
        # print(column)
        # print(sboxArray[i-1][row][column])

        b = bin(sboxArray[i-1][row][column])[2:]
        while (len(b) < 4):
            b = "0" + b

        # print("-------")
        newString = newString + b
    # print(len(newString))
    return newString

def straightPerm(a):
    permArray = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    newString = ""
    for i in permArray:
        newString = newString + a[i-1]
    return newString


def finalPermutation(stringBit):
    finalArray = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    newString = ""
    for i in finalArray:
        newString = newString + stringBit[i-1]
    return newString

# code for key generation
# key of length 48 bits
def generateKey(keyBit, round):
    a = shiftLeft(keyBit, round)
    a = compressionBox(a)
    # print(round)
    return a

def parityDrop(keyBit):
    # k = ""
    # for i in range(len(keyBit)):
    #     if ((i+1)%8 != 0):
    #         k += keyBit[i]
    permutatedKey = ""
    pTable = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    for i in pTable:
        permutatedKey += keyBit[i-1]
    return permutatedKey

# round will range from 0 to 15
def shiftLeft(keyBit, round):
    left = keyBit[:28]
    right = keyBit[28:]
    roundTable = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    shift = roundTable[round]
    # rotate the left and right key
    newLeft = left[shift:] + left[0:shift]
    newRight = right[shift:] + right[0:shift]
    return newLeft + newRight

def compressionBox(keyBit):
    compressionTable = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    key = ""
    for i in compressionTable:
        key += keyBit[i-1]
    return key

# decoder
# read in cipheredText binary string
cipheredText = open("cipheredText.txt", "r").read()
# cipheredText = stringToBits(cipheredText)
try:
    k = sys.argv[1]
    byteK = k.encode('utf-8')
    hexK = str(byteK.hex())
    key = hexToBits(hexK)
    key = parityDrop(key)
except:
    print("Please follow this format: python3 decoder.py [Key of length 64 bits]")

# generate key keySchedule
keySchedule = []
a = key
for i in range(16):
    keySchedule.append(generateKey(a, i))
    a = shiftLeft(a, i)

if (len(key) == 56):
    segments = []
    for i in range(int(len(cipheredText)/64)):
        segments.append(cipheredText[64*i:64*(i+1)])

    ansSegments = []
    # perform Feistel Cipher for each segment
    for s in segments:
        s = initialPermutation(s)
        # 16 rounds of f function
        for i in range(16):
            # reverse key schedule
            s = roundCalculation(s, 15-i, keySchedule[15-i])
            print("Decoder " + str(i))
            print(s)
        s = finalPermutation(s)
        ansSegments.append(s)
    a = ''.join(ansSegments)
    # print(len(ansSegments))
    # print(len(a))
    # print(a)
    # print(a)
    print(bitsToHex(a))
    f = open("decipheredText.txt", "w")
    f.write(a)
# else:
#     print("Please enter a key of length 64 bits.")









# Feistel Cipher Simulation
# def encoder(plainTextBit, keyBit):
#     finalBits = ""
#     for i in range(len(plainTextBits)/8):
#         x = initialPermutation(plainTextBits[8*i-8:8*i-1])
#         for i in range(16):
#             x = roundCalculation(x, i+1, keyBit)
#         x = finalPermutation(x)
#         finalBits = finalBits + x
#     return bitsToString(finalBits)

# def decoder(plainText, key):
#     plainTextBits = stringToBits(plainText)
#     if (len(plainTextBits) % 64 != 0):
#         plainTextBits = plainTextBits + ""
#     finalBits = ""
#     keyBit = stringToBits(key)
#     for i in range(len(plainTextBits)/8):
#         x = initialPermutation(plainTextBits[8*i-8:8*i-1])
#         for i in range(16):
#             x = roundCalculation(x, 16-i, keyBit)
#         x = finalPermutation(x)
#         finalBits = finalBits + x
#     return bitsToString(finalBits)

# try:
    # plainText = stringToBits(sys.argv[1])
    # apend 0s to the end to make len(plainText) a multiple of 64. This will make the operations below easier to handle
    # if (len(plainText)%64 != 0):
    #     for i in range(64-len(plainText)%64):
    #         plainText += "0"
    # key = stringToBits(sys.argv[2])
# except:
#     print("Please follow this format: python3 encoder.py [Plain Text] [Key of length 64 bits]")

# encoder using Feistel Cipher
# if (len(key) == 64):
#     # divide plaintext into subgroups of 64
#     segments = []
#     for i in range(int(len(plainText)/64)):
#         segments.append(plainText[64*i:64*(i+1)])
#
#     ansSegments = []
#     keySchedule = []
#     # perform Feistel Cipher for each segment
#     for s in segments:
#         s = initialPermutation(s)
#         # 16 rounds of f function
#         for i in range(16):
#             s = roundCalculation(s, i, key)
#         s = finalPermutation(s)
#         ansSegments.append(s)
#     a = ''.join(ansSegments)
#     print(bitsToString(a))

# else:
#     print("Please enter a key of length 64 bits.")
