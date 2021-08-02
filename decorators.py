'''Python passes based on the objects
    Decorators can be used to validate the functions witout modifying the underlying functions.
'''
def func(eb):
    def wrapper(*args, **kwargs):
        print("started")
        var = eb(*args, **kwargs)
        print("Ended")
        return var

    return wrapper

# This decorators takes mentioned function below as a parameters
@func
def func2(y):
    print("Inside func2")
    return y

@func
def func3(x):
    print(f"Inside func3 value is {x}")
# x = func(func2)
# print(x)
# x()
# func2 = func(func2) #same as @func that is decorators
# func2()
func3(4)
s = func2(7)
print(s)
