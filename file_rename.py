import os

folderPath = "C:\\Users\\422470\\PyCharmProjects\\BMRCL\\output\\IDC"
for mod in ["\\CBI", "\\SigRule", "\\SigRule-VDU", "\\TrackPlan", "\\Root", "", "\\Group"]:
    path = folderPath + mod
    filesList = [os.path.join(path, f) for f in os.listdir(path)]
    for file in filesList:
        if "_A.xml" in file:
            dest_path = file.replace("_A.xml", "_15368.xml")
            try:
                os.remove(dest_path)
            except FileNotFoundError:
                pass
            os.rename(file, dest_path)
        elif "_MYRD" in file:
            dest_path = file.replace("_MYRD", "_111")
            try:
                os.remove(dest_path)
            except FileNotFoundError:
                pass
            os.rename(file, dest_path)