import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    iteration = 0
    for i, elem in enumerate(q):
        if i - elem + 1 < -2:
            print('Too chaotic')
            return
    for no in range(len(q) - 1, -1, -1):
        for i in range(max(0, q[no] - 2), no):
            if q[i] > q[no]:
                iteration += 1
    print(iteration)

if __name__ == '__main__':
    print("Enter count")
    t = int(input())
    for t_itr in range(t):
        # n = int(input())
        print("Enter array")
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)