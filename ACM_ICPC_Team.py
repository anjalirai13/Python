from itertools import combinations

# Complete the acmTeam function below.
def acmTeam(topic):
    max_subjects = []
    comb = combinations(topic, 2)
    for x in comb:
        max_subjects.append(str(bin(int(x[0],2)|int(x[1],2)))[2:].count('1'))
    max_marks = max(max_subjects)
    return max_marks, max_subjects.count(max_marks)

n = 4
m = 5
array = ['10101', '11100', '11010', '00101']
print(acmTeam(array))