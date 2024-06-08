class Shape:
    def __init__(self,colour,opacity,a,b):
        self.colour=colour
        self.opacity=opacity
        self.centre=(a,b)
    def change_colour(self,colour):
        self.colour=colour
    def display(self):
        print('mycolor',self.colour)
        print('myopacity',self.opacity)
        print('my x coordinate',self.centre[0])
        print('my y coordinate',self.centre[1])

class Circle(Shape):
    def __init__(self,color, opacity, a, b, radius):
        Shape.__init__(self, color, opacity, a, b)
        self.radius=radius



circle=Circle('red',2,0,0, 10)
rect=Shape('blue',1,5,8)
circle.change_colour('green')
circle.display()
rect.display()


