with open("sample_write_text", mode="a+") as fd:
    fd.write("I want to see if I can read and write this text\n")
    fd.write("Writing another line\n")
    fd.seek(0)
    print(fd.read())
