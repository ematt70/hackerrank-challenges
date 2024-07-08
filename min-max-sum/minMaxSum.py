import numpy as np
import math

arr = [5,5,5,5,5]

arr.sort()
minSum = 0

if len(arr) == 0:
    minSum = 0
else:
    for index, element in enumerate(arr):
        if index < len(arr) - 1:
            minSum = minSum + element


maxSum = 0

if len(arr) == 0:
    maxSum = 0
else:
    arr.sort(reverse=True)
    for index, element in enumerate(arr):
        if index < len(arr) - 1:
            maxSum = maxSum + element

minMaxSums = str(minSum) + " " + str(maxSum)
print(minMaxSums)