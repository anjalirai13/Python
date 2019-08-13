def birthdayCakeCandles(arr):
    max_val = max(arr)
    print(arr.count(max_val))

arr = [int(x) for x in ('3 2 1 3').strip().split()]
birthdayCakeCandles(arr)