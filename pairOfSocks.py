# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_dict = {}
    pair_count = 0
    for i in range(0, n):
        if not sock_dict.get(ar[i]):
            sock_dict[ar[i]] = 1
        else:
            sock_dict[ar[i]] += 1
    for sock, count in sock_dict.items():
        pair_count += int(sock_dict[sock]/2)
    return pair_count


no = 9
sock_arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(no, sock_arr))