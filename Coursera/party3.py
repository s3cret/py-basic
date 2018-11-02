class PartyAnimal:
    x = 0

    # this is one of the PartyAnimal class function
    def party(self) :
        self.x = self.x + 1
        print("Atendding party ...",self.x)
# init a PartyAnimal instance and assign it to `an`
an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))
