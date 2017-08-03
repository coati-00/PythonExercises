#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # get tallest candle, if there are several tall candles - count them
    tallest = ar[0]
    count = 1

    # going to do this the long way, and improve later
    for index in range(0,len(ar),+1):
        '''start by looking for tallest candle'''
        if ar[index + 1] > ar[index]:
            tallest = ar[index + 1]
    print tallest
    for each in ar:
        if each == tallest:
            count = count + 1
    print count
    # print count
    return count
        
        
        
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)


'''
Sample Input:
4
3 2 1 3
'''