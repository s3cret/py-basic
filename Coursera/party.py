class PartyAnimal:
    # these are two variables in this simple class
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'is constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

# this is raw class file, nothing to do
