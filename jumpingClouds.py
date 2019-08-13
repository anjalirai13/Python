# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    minSteps = 0
    index = 0
    for i in range(len(c)-1):
        if index == i:
            if i+2 < len(c) and (c[i+2] == 0):
                index = i+2
                minSteps +=1
            elif i+1 <= len(c) and (c[i+1] == 0):
                index = i+1
                minSteps += 1
    return minSteps

clouds = list('0 0 1 0 0 0 1'.split(" "))
cloud_arr = []
for c in clouds: cloud_arr.append(int(c))
print(jumpingOnClouds(cloud_arr))