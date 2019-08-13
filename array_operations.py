from array import *

arr = array('i', [10,20, 30, 40, 50])

for x in arr: print(x)

arr.insert(2, 60)
for x in arr: print(x)

arr.remove(60)
for x in arr: print(x)

print(arr.index(20))
for x in arr: print(x)

arr[2] = 60
for x in arr: print(x)