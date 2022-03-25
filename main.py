# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_1 = 0
    score_2 = 0
    
    for i in range (0, len(a)):
        print(len(a))
        if a[i] > b[i]:
            score_1 += 1
            
        if a[i] < b[i]:
            score_2 += 1
            
    return score_1, score_2

print(compareTriplets([17, 28, 30], [99, 16, 8]))