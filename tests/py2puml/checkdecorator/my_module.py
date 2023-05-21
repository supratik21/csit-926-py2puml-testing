def my_decorator(cls):
    class NewClass(cls):
        pass
    return NewClass

@my_decorator
class MyClass:
    attribute1: str
    attribute2: int
