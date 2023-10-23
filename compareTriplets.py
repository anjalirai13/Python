
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    res = [0, 0]
    for no in range(len(a)):
        if a[no] > b[no]:
            res[0] += 1
        elif a[no] < b[no]:
            res[1] += 1
    return res