class Person:
    def __init__(self, name):
        self.name = name


    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')
p.say_hi()
# The following code get an error.
# Missing one required positional argument.
# q = Person()
# q.say_hi()
