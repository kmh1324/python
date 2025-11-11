class Circle:
    PI = 3.141592
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * self.radius * Circle.PI

class Cylinder:
    def __init__(self, Circle, height):
        self.Circle = Circle
        self.height = height

    def get_volume(self):
        return self.Circle.get_area() * self.height
    
cylinder = Cylinder(Circle(2.8), 5.6)
print(cylinder.get_volume())


