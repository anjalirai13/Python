list = [-4, 3, -9, 0, 4, 1]

pos_count = 0
neg_count = 0
zero_count = 0

for no in list:
    if no == 0:
        zero_count +=1
    elif no > 0:
        pos_count += 1
    elif no < 0:
        neg_count += 1

print(round(pos_count/len(list), 6))
print(round(neg_count/len(list), 6))
print(round(zero_count/len(list), 6))