import random
import sys
import codecs

#64 Bit -> 64 Bit
#string to convert
#Key to convert
#string -> bit string

def stringToBits(str):
    stringBit = ""
    for i in range(len(str)):
        asciiValue = ord(str[i])  
        binValue = bin(asciiValue)[2:]
        for i in range(8 - len(binValue)):
            binValue = "0" + binValue
        stringBit = stringBit + binValue
    return stringBit

def bitsToString(str):
    finString = ""
    for i in range(len(str)/8):
        asciiValue = int(str[i*8-8:i*8-1], 2)
        finString = finString + chr(asciiValue)
    return finString

def initialPermutation(stringBit):
    initialArray = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    newString = ""
    for int i in range(64):
        newString = newString + stringBit[initialArray[i])]
    return newString

#64 bit -> 64 bit
def round(stringBit, curRound):
    a = stringBit[32:] + (ffunction(stringBit[32:], curRound) ^ stringBit[0:31])
    return a

def ffunction(right, curRound):
    a = expansion(right)
    a = a ^ generateKey(curRound)
    a = sbox(a)
    a = straightPerm(a)
    return a

def expansion(right):
    expanArray = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 31, 31, 32, 1]
    newString = ""
    for i in range(48):
        newString = newString + right[expanArray[i]]
    return newString

def sbox(a):
    sboxArray = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    newString = ""
    row = 0
    column = 0
    for i in range(8):
        row = int(a[6*i-6] + a[6*i-1])
        column = int(a[6*i-5] + a[6*i-4] + a[6*i-3] + a[6*i-2])
        newString = newString + bin((sboxArray[row])[column])[2:]
    return newString

def straightPerm(a):
    permArray = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    newString = ""
    for i in range(32):
        newString = newString + a[permArray[i]]
    return newString


def finalPermutation(stringBit):
    finalArray = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    newString = ""
    for int i in range(64):
        newString = newString + stringBit[finalArray[i])]
    return newString


