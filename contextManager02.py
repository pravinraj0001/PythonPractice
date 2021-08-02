from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print('Enter')
    file = open(filename, method)
    yield file
    file.close()
    print("Exit")

with file("text.txt", "w") as f:
    print("Middle")
    f.write("hello")
