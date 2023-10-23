# Complete the permutationEquation function below.
def permutationEquation(p):
    arr = []
    for x in range(1, len(p)+1):
        y = p.index(x) + 1
        arr.append(p.index(y)+1)
    return arr

print(permutationEquation([2,3,1]))
print(permutationEquation([4,3,5,1,2]))
