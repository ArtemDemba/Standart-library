import abc


class Shape(abc.ABC):   # This inheritance bans ability of creating objects of this abstract class

    def __init__(self):
        super().__init__()

    @abc.abstractmethod # This decorator bans ability of calling this method and make all subclasses
    def draw(self):     # of this abstract class to implement this method
        pass

    @abc.abstractmethod
    def say_hello(self):
        print('Say hello from abstract class')  # We can add an implementation to the abstract method

    def some_other_method(self):    # This method isn't abstract, and it can not be inherited by subclasses
        print(self.__class__)


class Square(Shape):
    def draw(self):
        print('Draw square')

    def say_hello(self):
        super(Square, self).say_hello() # We can call base abstract method with its implementation
        print('Hello')

    def some_other_method(self):
        super(Square, self).some_other_method()


if __name__ == '__main__':
    s = Square()
    s.say_hello()

