# Complete the pairs function below.
def pairs(k, a):
    count = 0
    temp_arr = set(a)
    for x in a:
        if k+x in temp_arr: count += 1
    return count

k = 2
a = [1,5,3,4,2]

print(pairs(k, a))