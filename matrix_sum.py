def diagonalDifference(arr):
    # Write your code here
    arr_length = len(arr)-1
    diagonal_1 = 0
    diagonal_2 = 0
    for no in range(arr_length+1):
        diagonal_1 += arr[no][no]
        diagonal_2 += arr[no][arr_length-no]
    return abs(diagonal_1 - diagonal_2)

arr = []