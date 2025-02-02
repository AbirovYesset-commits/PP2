class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length
    def area(self):
        return self.length ** 2
    
class Reqtangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.lenght=length
        self.width=width
    def area(self):
        return self.lenght*self.width

shape=Shape()
print(shape.area())

square=Square(5)
print(square.area())

reqtangle=Reqtangle(4, 6)
print(reqtangle.area)

    


