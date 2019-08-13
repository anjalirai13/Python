# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    stepCount = 0
    for i in range(len(s)):
        if s[i] == 'U':
            stepCount += 1
            if stepCount == 0: valleyCount += 1
        elif s[i] == 'D':
            stepCount -= 1
    return valleyCount


no = 8
steps = 'UDDDUDUU'
print(countingValleys(no, steps))