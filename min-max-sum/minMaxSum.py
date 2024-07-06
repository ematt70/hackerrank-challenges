import numpy as np
import math

arr = [5,9,2,4,6]

arr.sort()
minSum = 0

if len(arr) == 0:
    minSum = 0
else:
    for x in arr:
        if arr.index(x) < len(arr) - 1:
            minSum = minSum + x


maxSum = 0

if len(arr) == 0:
    maxSum = 0
else:
    arr.sort(reverse=True)
    for y in arr:
        if arr.index(y) < len(arr) - 1:
            maxSum = maxSum + y

minMaxSums = str(minSum) + " " + str(maxSum)
print(minMaxSums)


