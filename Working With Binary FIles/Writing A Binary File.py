import pickle
d = {"Name: ": "Akshat", "Roll: ": "05", "Marks: ": "100"}
d2 = {"Name: ": "AKSHAT", "Roll: ": "10", "Marks: ": "0"}
l = list()
l.append(d)
l.append(d2)
MyFile = open("sample.bin", "wb")
pickle.dump(l, MyFile)
MyFile.close()
