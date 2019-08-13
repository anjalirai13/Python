import os
import re
test_case_array = []
files_list = []
filePath = 'C:\\work\\ams\\ccsp_ase-ccsp_ase-dexter_ams\\validation\\'

complete_dir_path = [x for x in os.walk((filePath))]
for p in complete_dir_path:
    if p[2]:
        for name in p[2]:
            if ".cpp" in name[-4:]:
                files_list.append(os.path.join(p[0], name))

for f in files_list:
    with open(f, 'r', encoding='utf-8') as test_file:
        test_file_name = False
        try:
            comment_str = ("\n\n-------#################################---------------\n" + f + "\n-------#################################---------------\n")
            length = len(test_case_array)
            for line in test_file.readlines():
                if "TEST_F" in line:
                    test_case_array.append(line.split(",")[1].replace(")", '').replace(" ", ''))
                    test_file_name = True
            if test_file_name:
                test_case_array.insert(length, comment_str)
        except:
            print("Unable to parse file ", f)

with open("./test_details.txt", 'w') as test_file:
    for test_case in test_case_array:
        test_file.write(test_case)
    test_file.close()