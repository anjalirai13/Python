def countApplesAndOranges(s, t, a, b, apples, oranges):
    result = [0, 0]
    for fall in apples:
        if (fall+a) in range(s, t+1): result[0] +=1
    for fall in oranges:
        if (fall+b) in range(s, t+1): result[1] +=1
    for val in result:
        print(val)

s_t = '2 3'.split(" ")
a_b = '1 5'.split(" ")
# m_n = [int(x) for x in '3 2'.split(" ")]
s = int(s_t[0])
t = int(s_t[1])
a = int(a_b[0])
b = int(a_b[1])

apple_fall = [int(x) for x in '2'.split(" ")]
orange_fall = [int(x) for x in '-2'.split(" ")]
countApplesAndOranges(s, t, a, b, apple_fall, orange_fall)