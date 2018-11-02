class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("Attending party ...", self.x)
# init a PartyAnimal instance and assign it to `an`
an = PartyAnimal()
# call party() function three times
an.party()
an.party()
an.party()
# it is exactly what the word `self` does when calling a function
PartyAnimal.party(an)
