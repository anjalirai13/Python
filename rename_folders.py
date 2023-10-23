import os

logs_path = "C:\\Logs"

dirs = []
for subdir, dir, files in os.walk(logs_path):
    for f in files:
        if "data_collection.csv" in f:
            f_name = f.split(".")[0] + "_defender.csv"
            nf_name = os.path.join(subdir, f_name)
            of_name = os.path.join(subdir, f)
            # os.rename(r'{}'.format(f_name), r'{}'.format(nf_name))
            try:
                os.rename(of_name, nf_name)
            except:
                pass

for dir in os.listdir(logs_path):
    od_name = os.path.join(logs_path, dir)
    nd_name = od_name + "_defender"
    try:
        os.rename(od_name, nd_name)
    except:
        pass