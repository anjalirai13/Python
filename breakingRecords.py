# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_record = scores[0]
    min_record = scores[0]
    record_break = [0, 0]
    for score in scores:
        if score > max_record:
            max_record = score
            record_break[0] +=1
        if score < min_record:
            min_record = score
            record_break[1] +=1
    return (record_break[0], record_break[1])

scores = [10,5,20, 20,4,5,2,25,1]
print(breakingRecords(scores))