class Animal:
    '''
    This is Animal class doc
    '''
    def __init__(self, name=''):
        print('An Animal is being built ...')
        self.__name = name

    def run(self):
        print('Animal is running ...')

    def get_name(self):
        return self.__name


class Cat(Animal):
    def run(self):
        print('Mew Mew Mew ~~~')
    def eat(self):
        print('Cat is eating ...')


class Dog(Animal):
    def run(self):
        print('woof! woof!')
    pass


class Runky(Dog):
    def __init__(self):
        Animal.__init__(self, "Runky")

    pass
