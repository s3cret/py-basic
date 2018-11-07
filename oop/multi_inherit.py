class Parent1(object):
    def func(self):
        print('func from parent1')

class Parent2(object):
    def func(self):
        print('func from parent2')

# call the first class's same-name function
class Child(Parent2, Parent1):
    pass

c = Child()
c.func()
