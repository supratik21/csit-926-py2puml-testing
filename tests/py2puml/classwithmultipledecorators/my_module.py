def my_decorator1(cls): 
    class NewClass1(cls): 
        pass
    return NewClass1 
def my_decorator2(cls): 
    class NewClass2(cls): 
        pass 
    return NewClass2 
@my_decorator1 
@my_decorator2 
class MyClass: 
    attribute1: str 
    attribute2: int