from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def foo(self):
        pass


_b_initial_class_variable = 0


class B(A):
    class_variable = _b_initial_class_variable

    def foo(self):
        print("bar")


if __name__ == "__main__":
    # int
    foo = 5
    print(type(foo))

    print(A.__subclasses__())

    try:
        a1 = A()  # type: ignore
        print(a1)
    except TypeError as e:
        print(e)

    b1 = B()
    assert b1.class_variable == _b_initial_class_variable

    B.class_variable = 1
    assert b1.class_variable == 1

    b2 = B()
    b2.class_variable = 2
    assert b1.class_variable == 1

    # delattr(A, "foo")
    # a2 = A()
