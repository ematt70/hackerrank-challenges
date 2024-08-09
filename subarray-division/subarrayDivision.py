import math

segments = [2, 2, 1, 3, 2]
day = 4
month = 2

def birthday(s, d, m):
    
    total = 0
    for index, segment in enumerate(s):
        if len(s) - m < index:
            break
        else:
            segmentSum = 0
            for i in range(0, m):
                segmentSum += s[i]
            if segmentSum == d:
                total += 1
    return total

print(birthday(segments, day, month))