def fibonacciModified(seq):
    n = seq[2]
    arr = [seq[0], seq[1]]
    for i in range(n):
        arr.append(arr[i]+arr[i+1]**2)
    print(arr[4])

seq = [int(x) for x in '0 1 5'.strip().split()]
fibonacciModified(seq)