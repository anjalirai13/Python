# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    count = 0
    comp_len = min(len(s), len(t))
    for i in range(comp_len):
        if (t[i] == s[i]):
            count +=1
        else:
            break
    diff = len(s) - count + len(t) - count
    if (diff <= k) and ((k-diff)%2==0) or (len(s)+len(t)<k):
        return "Yes"
    else:
        return "No"

print(appendAndDelete("hackerhappy", "hackerrank", 9))