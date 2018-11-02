class PartyAnimal:
    # these are two variables in class PartyAnimal
    x = 0
    name = ''
    # init function with a parameter name `name`
    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name, 'Attending party ...', self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

# call function
s.party()
j.party()
s.party()

