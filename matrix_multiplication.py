def matrix_multiplication(nrows, arr1, arr2):
    out = []

    if len(arr1) != len(arr2):
        return "Insufficient data"
    for row in range(nrows):
        res = []
        for col in range(nrows):
            res.append(sum([arr1[row][cell]*arr2[cell][row] for cell in range(nrows)]))
        out.append(res)
    for i in range(nrows):
        print(" ".join([str(i) for i in out[i]]))

def get_input(nrows):
    arr = []
    print("Enter values for matrix separated by space\n")
    for i in range(nrows):
        values = input()
        values = [int(val) for val in values.split(" ")]
        if (len(values)) != nrows:
            print("Incorrect no of values specified")
            exit()
        arr.append(values)
    return arr

if __name__ == "__main__":
    nrows = int(input("Enter the no of rows\n"))
    arr1 = []
    arr2 = []
    arr1 = get_input(nrows)
    arr2 = get_input(nrows)
    matrix_multiplication(nrows, arr1, arr2)
    # nrows = 4
    # arr1 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    # arr2 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    # matrix_multiplication(nrows, arr1, arr2)

