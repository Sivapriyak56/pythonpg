
class Rectangle:
    def _init_(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self._length * self._width

    def _lt_(self, other):
        return self.area() < other.area()


l1 = int(input("Enter the length of first rectangle"))
w1 = int(input("Enter the width of second rectangle"))
rectangle1 = (l1, w1)
l2 = int(input("Enter the length of first rectangle"))
w2 = int(input("Enter the width of second rectangle"))
rectangle2 = (l2, w2)
# r1 = Rectangle(4, 5)
# r2 = Rectangle(6, 3)
if rectangle1 < rectangle2:
    print("Area of rectangle 1 is smaller")
else:
    print("Area of rectangle 2 is smaller")