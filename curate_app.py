import subprocess
from functools import partial

child = subprocess.Popen(['app.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
# child = subprocess.Popen(['app.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

count = 0
# iterate while child is not terminated
while child.poll() is None:
    line = ''
    # read stdout character by character until a colon appears
    for c in child.stdout.readline():
        if c == ':':
            break
        line += c
    if "enter sum" in line:
        numbers = filter(str.isdigit, line.split())
        numbers = list(map(int, numbers))
        child.stdin.write("Ctrl+C\n".format(sum(numbers)))
        child.stdin.write("{0}\n".format(sum(numbers)))
        child.stdin.flush()
        print("entered ", sum(numbers))