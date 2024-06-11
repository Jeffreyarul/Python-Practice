import classes_objects

class Vehicle:
    def __init__(self,tyres,seats,capacity):
        self.tyres=tyres
        self.seats=seats
        self.capacity=capacity
    
    def display(self):
        print("no of tyres=",self.tyres)
        print("no of seats=",self.seats)
        print("capacity of vehicle=",self.capacity)

    def calculate_milage(self,dist):
        self.milage=dist/self.capacity

class Truck(Vehicle):

    def __init__(self,capacity,make):
        super().__init__(8,2,capacity)
        self.make=make

    def display(self,dist):
        print("no of tyres=",self.tyres)
        print("no of seats=",self.seats)
        print("capacity of vehicle=",self.capacity)
        print("made in ",self.make)
        print("mileage = ",self.milage)

c=Vehicle(4,4,35)
c.display()
c.calculate_milage(500)
print(c.milage)
b=Truck(30,2002)
b.calculate_milage(400)
b.display(dist=250)
classes_objects.main()
r=classes_objects.Rectangle(5,8)
r.calc_Area()
r.calc_peri()
print(r.peri)
