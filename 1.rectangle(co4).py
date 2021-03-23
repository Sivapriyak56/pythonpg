class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
r1=Rectangle(5,7)
r2=Rectangle(10,20)
a=r1.area()
print("area of r1",+a)
a1=r2.area()
print("area of r2",+a1)
b=r1.perimeter()
print("perimeter of r1",+b)
b1=r2.perimeter()
print("perimeter of r2",+b1)
if a<a1:
    print("Rectangle r2 is greater")
else:
    print("rectangle r1 is greater")
