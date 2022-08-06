import pickle

# declaration and initialization
l = []
n = int(input("Number of student info. to be entered: "))

# for loop to collect student information
for i in range(0, n):
    name = input("Name: ")
    roll = input("Roll: ")
    marks = input("Marks: ")
    d = dict()
    d["Name: "] = name
    d["Roll No.: "] = roll
    d["Marks: "] = marks
    l.append(d)
    del d

# creating file object and writing information into the file
MyFile = open("StudentInformation.bin", "wb")
pickle.dump(l, MyFile)
MyFile.close()
