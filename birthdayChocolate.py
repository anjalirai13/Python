# Complete the birthday function below.
def birthday(s, d, m):
    total_count = 0
    for x in range(0, len(s)):
        total = s[x]
        for y in range(0, m-1):
            if x+y < len(s)-1:
                total += s[x+y+1]
        if total == d: total_count += 1
    return total_count

s = [1, 2, 1, 3, 2]
d = 3
m = 2

print(birthday(s, d, m))