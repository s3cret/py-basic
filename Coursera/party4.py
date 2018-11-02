# shows the basic __init__ fucntion and __del__ function
class PartyAnimal:
    x = 0
    def __init__(self):
        print('Constructing ...')

    def party(self) :
        self.x = self.x + 1
        print('Attending party ...', self.x)

    def __del__(self):
        print('Destructing ...', self.x)
# init an instance of PartyAnimal class and assign it to `an`
an = PartyAnimal()
# call function party() twice
an.party()
an.party()
# variable an can be assigned to another things as below
print('change the variable an to an int number')
# it will automatically call the __del__ function
an = 42
print('an contains', an)
