class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print("Exit")
        self.file.close()


with File("file.txt","w") as f:
    print("Middle")
    f.write("Hello! Pravin")
