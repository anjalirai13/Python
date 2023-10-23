file_1 = "result_1.log"
file_2 = "result_2.log"

fd1 = open(file_1)
fd1_contents = fd1.readlines()

fd2 = open(file_2)
fd2_contents = fd2.readlines()

for no in range(len(fd1_contents)):
    if "PASSED" in fd1_contents[no] and "PASSED" in fd2_contents[no]:
        pass
    elif "PASSED" in fd1_contents[no] and "SKIPPED" in fd2_contents[no]:
        print(fd1_contents[no].strip())