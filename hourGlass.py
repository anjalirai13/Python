def hourglass(arr):
    add_arr = []
    for x in range(0, len(arr)-2):
        for y in range(0, len(arr[x])-2):
            value = arr[x][y] + arr[x][y+1] + arr[x][y+2]
            value += arr[x+1][y+1]
            value += arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            add_arr.append(value)
    return max(add_arr)

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

print(hourglass(arr))
