class Rectangle:
    def __init__(self, l, w):  
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
    

# Creating an object 
rectangle = Rectangle(10,5)


#  attribute
print(rectangle.l)
print(rectangle.w)

Area = rectangle.area()
print("Area of the rectangle:", Area)