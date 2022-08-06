import pickle

MyFile = open("StudentInformation.bin", "rb")
l = pickle.load(MyFile)
MyFile.close()

y = 'y'
while y == 'y':
    n = int(input("Student S.No: "))
    index = n-1
    d = l[index]
    print(f'Name: {d["Name: "]}\n'
          f'Roll No: {d["Roll No.: "]}\n'
          f'Marks: {d["Marks: "]}\n')
    del d

    y = input("y -> continue\nn -> exit\n")
