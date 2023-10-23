arr1 = [
{'data_type': 'float32', 'rows': 10000000, 'columns': 20, 'time': 1.062426244100789},
{'data_type': 'float64', 'rows': 10000000, 'columns': 20, 'time': 1.774223540502135},
{'data_type': 'float32', 'rows': 2000000, 'columns': 100, 'time': 1.649226554282775},
{'data_type': 'float64', 'rows': 2000000, 'columns': 100, 'time': 3.405863029989026}]

res = [{key : val for key, val in sub.items() if key != 'time'} for sub in arr1]

x2 = {'data_type': 'float32', 'rows': 10000000, 'columns': 20}
print(res)
print(x2 in res)
print(res.index(x2))