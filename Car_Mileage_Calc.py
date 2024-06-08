class Car:
    def __init__(self,dist,fuel):
        self.dist=dist
        self.fuel=fuel
        self.mil=0
        self.money=0
    
    def mileage(self):
        self.mil=self.dist/self.fuel
    
    def bonus(self):
        if self.mil > 15 :
            self.money = 1000
        elif self.mil > 10:
           self.money = 550
        else:
           self.money =200      

def main():
    venue=Car(3000,35)
    i20=Car(10000,55)
    venue.mileage()
    print(venue.mil)
    i20.mileage()
    print(i20.mil)
    venue.bonus()
    print(venue.money)
    i20.bonus()
    print(i20.money)

main()