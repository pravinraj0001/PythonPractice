# Complicated and bad practice unless we abolutely needed to.
# meta class inherits from the type

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8
    def hello(self):
        print("hi")
d = Dog()
d.HELLO()
