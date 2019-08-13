# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count('a')*n//len(s)+ s[:n % len(s)].count('a')

string = 'a'
no = 1000000000000
print(repeatedString(string, no))