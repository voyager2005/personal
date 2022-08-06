import pickle

MyFile = open("sample.bin", "rb")
d = dict()
try:
    while True:
        d = pickle.load(MyFile)
except EOFError:
    print("Reached end of file")
    print(d)
MyFile.close()
