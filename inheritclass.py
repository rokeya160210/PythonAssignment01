
class Vehicle:
  def __init__(self, max_speed, mileage,seating_capacity):
    self.max_speed = max_speed
    self.mileage = mileage
    self.seating_capacity=seating_capacity
    

  def Charge(self):
    fareAmount = self.seating_capacity*100
    print(fareAmount)


class Bus(Vehicle):
  
  def __init__(self):
    Vehicle.__init__(self, 50, 60,50)
    self.max_speed = 50
    self.mileage = 60
    self.seating_capacitym =50
    

  def Charge(self):    
    fareAmount = (self.seating_capacity*100)   
    total = int(fareAmount +fareAmount * 0.1)
    print(total)

x = Bus()
v = x.Charge()


