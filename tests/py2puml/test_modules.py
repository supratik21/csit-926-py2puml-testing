from abc import ABC, abstractmethod
from hypothesis import given
from hypothesis.strategies import text, characters, just, one_of, integers
import pytest


class ClassTemplate(ABC):
    @abstractmethod
    def must_be_implemented(self):
        """ Docstring."""

class ConcreteClass(ClassTemplate):
    def must_be_implemented(self):
        pass

def test_creating_object_of_abstract_class_should_raise_error():
    try:
        obj = ClassTemplate()
    except TypeError:
        assert True
    else:
        assert False

def test_creating_object_of_concrete_class_should_not_raise_error():
    try:
        obj = ConcreteClass()
    except TypeError:
        assert False
    else:
        assert True

def test_concrete_class_instance_is_instance_of_class_template():
    obj = ConcreteClass()
    assert isinstance(obj, ClassTemplate)

def test_concrete_class_implements_must_be_implemented_method():
    obj = ConcreteClass()
    assert hasattr(obj, 'must_be_implemented')

def test_calling_must_be_implemented_on_concrete_class_does_not_raise_error():
    obj = ConcreteClass()
    obj.must_be_implemented()
    assert True

def test_calling_must_be_implemented_on_my_class_raises_no_error():
    class MyClass(ClassTemplate):
        def must_be_implemented(self):
            pass
    obj = MyClass()
    obj.must_be_implemented()
    assert True