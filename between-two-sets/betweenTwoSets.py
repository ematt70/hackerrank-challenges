import math

arr1 = [2, 4]
arr2 = [16, 32]

def getTotalX(a, b):
    
    count = 0
    for i in range(max(a), min(b) + 1):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            count += 1
    return count


print(getTotalX(arr1, arr2))



