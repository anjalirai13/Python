def staircase(stair_count):
    no = int(stair_count)
    for n in range(1, no+1):
        print(" "*(no-n)+"#"*n)

stair_count = input("Enter the staircase count")
staircase(stair_count)