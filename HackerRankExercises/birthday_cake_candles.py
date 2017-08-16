#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # get tallest candle, if there are several tall candles - count them
    tallest = ar[0]
    count = 0

    # going to do this the long way, and improve later
    for number in ar:
        if number > tallest:
            tallest = number

    for each in ar:
        if each == tallest:
            count = count + 1

    return count



n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
