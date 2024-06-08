class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.area = 0
        self.peri=0
    
    def calc_Area(self):
        self.area = self.length * self.width

    def calc_peri(self):
        self.peri = 2*(self.length+self.width)
    
def main():
    r = Rectangle(4, 5)
    print(r.area)
    r.calc_Area()
    print(r.area)
    r1=Rectangle(10,5)
    r1.calc_peri()
    print(r1.peri)
    


if __name__ == '__main__':
    main()