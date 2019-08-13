def kangaroo(x1, v1, x2, v2):
    try:
        divisor = (x1-x2)%(v2-v1)
        res = (x1-x2)/(v2-v1)
        result = "YES" if (divisor == 0 and res > 0) else "NO"
    except:
        result = "NO"
    return result

print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
print(kangaroo(43, 2, 70, 2))
