import math

def breakingRecords(scores):

    score = 0
    numRecsMinScore = 0
    numRecsMaxScore = 0
    
    for index, score in enumerate(scores):
        if index == 0:
            minScore = score
            maxScore = score
        else:
            if score < minScore:
                minScore = score
                numRecsMinScore += 1
            elif score > maxScore:
                maxScore = score
                numRecsMaxScore += 1
            else:
                continue
    
    records = [numRecsMaxScore, numRecsMinScore]
    return records

perf = [10, 5, 20, 4, 5, 2, 25, 1]

print(breakingRecords(perf))

