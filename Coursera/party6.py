from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   # in the function below call party() one time
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name, "points", self.points)

# s = PartyAnimal("Sally")
# s.party()
j = CricketFan("Jim")
# call parent method party()
#j.party()
# call its own method twice
j.six()
j.six()
#print(dir(j))
