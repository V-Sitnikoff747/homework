import math
import json

class Circle:
    radius=0
    def __init__(self, radius):
        self.radius=radius

    def length(self):
        return 2* math.pi*self.radius
    
    def __eq__(self, value):
        return self.radius== value.radius
        
    def __gt__(self, other):
        return self.length() > other.length()

    def __lt__(self, other):
        return self.length() < other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __le__(self, other):
        return self.length() <= other.length()
    
    def __add__(self, delta):
        return Circle(self.radius+delta)
        
    def __sub__(self, delta):
        return Circle(self.radius-delta)
    
    def __iadd__(self,delta):
        self.radius +=delta
        return self
        
    
    def __isub__(self, delta):
        self.radius-=delta
        return self
    
    def __isub__(self, delta):
        self.radius -= delta
        return self

    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
class Complex:
    re=0
    im=0
    def __init__(self, re, im):
        self.re=re
        self.im=im
    
    def __add__(self, value):
        return Complex(self.re+ value.re, self.im + value.im)
    
    def __sub__(self, value):
        return Complex(self.re - value.re, self.im - value.im)
    
    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im,
                       self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        denom = other.re ** 2 + other.im ** 2
        return Complex((self.re * other.re + self.im * other.im) / denom,
                       (self.im * other.re - self.re * other.im) / denom)

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else ''}{self.im}i)"
    
class Airplane:
    type_Plane=" "
    passengers=0
    maxPassengers=0
    def __init__(self,type_Plane, passengers,  maxPassengers ):
        self.type_Plane=type_Plane
        self.passengers=passengers
        self.maxPassengers=maxPassengers
    
    def __eq__(self, value):
        return self.type_Plane == value.type_Plane
        
    def __add__(self, value):
        newPassengers= self.passengers+value
        if newPassengers > self.maxPassengers:
            newPassengers=self.maxPassengers
        return Airplane(self.type_Plane, newPassengers, self.maxPassengers)
    
    def __sub__(self, value):
        newPassengers= self.passengers-value
        if newPassengers<0:
            newPassengers=0
        return Airplane(self.type_Plane, newPassengers, self.maxPassengers)
    
    def __iadd__(self, value):
        self.passengers+= value
        if self.passengers> self.maxPassengers:
            self.passengers=self.maxPassengers
        return self
    
    def __isub__(self, value):
        self.passengers-=value
        if self.passengers<0:
            self.passengers=0
        return self
    
    def __gt__(self, other):
         return self.maxPassengers > other.maxPassengers
    
    def __lt__(self, other):
        return self.maxPassengers < other.maxPassengers

    def __ge__(self, other):
        return self.maxPassengers >= other.maxPassengers

    def __le__(self, other):
        return self.maxPassengers <= other.maxPassengers

    def __repr__(self):
        return (f"Airplane(type='{self.type_Plane}', passengers={self.passengers}, f.maxPassengers={self.maxPassengers}")
    
class Flat:
    area=0
    price=0
    def __init__(self, area, price):
        self.area=area
        self.price=price
    
    def __eq__(self, other):
        return self.area==other.area
    
    def __ne__(self, other):
        return self.area != other.area
        
    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price
    
    def __ge__(self, other):
        return self.price >= other.price
    
    def __le__(self, other):
        return self.price <= other.price
    
    def __repr__(self):
        return f"Flat(area={self.area}, price={self.price})"
    
class Figure:
    def area(self):
        raise NotImplementedError
    
    def __int__(self):
        return int(self.area())
    
    def __str__(self):
        return f"{self.__class__.__name__} с площадью {self.area():.2f}"
        
class Rectangle(Figure):
    width=0
    height=0
    def __init__(self, width, height ):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
class Circle_1(Figure):
    radius=0
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return  math.pi * self.radius**2
    
class RightTriangle(Figure):
    base=0
    hight=0

    def __init__(self, base, hight):
        self.hight= hight
        self.base= base

    def area(self):
        return self.base* self.hight *0.5
    
class Trapezoid(Figure):
    base_1=0
    base_2=0
    hight=0

    def __init__(self, base_1, base_2, hight):
        self.base_1=base_1
        self.base_2=base_2
        self.hight=hight

    def area(self):
        return (self.base_1+self.base_2)*0.5*self.hight
            
class Shape:
    def show(self):
        print(str(self)) 
    def save(self, filename):
        with open(filename,'w') as f:
            json.dump(self.__dict__,f)  

    def load(self,filename):
        with open(filename,'r') as f:
            data=json.load(f)
            self.__dict__.update(data)     
            
class Square(Shape):
    x=0
    y=0
    side=0
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f"Square: левый верхний угол ({self.x}, {self.y}), сторона {self.side}"

    def area(self):
        return self.side ** 2

            
class Rectangle_1(Shape):
    x=0
    y=0
    width=0
    height=0

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: левый верхний угол ({self.x}, {self.y}), ширина {self.width}, высота {self.height}"

    def area(self):
        return self.width * self.height

class Circle_1(Shape):
    x=0
    y=0
    radius=0

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"Circle: центр ({self.x}, {self.y}), радиус {self.radius}"

    def area(self):
        return math.pi * self.radius ** 2

class Ellipse(Shape):
    x=0
    y=0
    width=0
    height=0
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Ellipse: верхний левый угол ({self.x}, {self.y}), ширина {self.width}, высота {self.height}"

    def area(self):
        return math.pi * (self.width / 2) * (self.height / 2)
    
def main():
    # Пример использования Circle
    c = Circle(5)
    print(c)  # Circle(radius=5)
    c += 2
    print(c)  # Circle(radius=7)
    
    # Пример использования Complex
    z1 = Complex(2, 3)
    z2 = Complex(1, -1)
    print(z1 + z2)  # (3+2i)
    print(z1 * z2)  # (5+1i)
    
    # Пример Airplane
    plane = Airplane("Boeing", 100, 200)
    print(plane)
    plane += 50
    print(plane)
    
    # Пример Flat
    flat1 = Flat(50, 100000)
    flat2 = Flat(60, 120000)
    print(flat1 > flat2)  # False

    # Пример Figure — Rectangle
    rect = Rectangle(10, 5)
    print(rect)
    print("Площадь:", rect.area())
    
    # Пример Shape — Square
    square = Square(0, 0, 4)
    square.show()
    print("Площадь квадрата:", square.area())
    
    # Можно сохранить и загрузить объект Square
    square.save('square.json')
    new_square = Square(0, 0, 0)
    new_square.load('square.json')
    new_square.show()

if __name__ == "__main__":
    main()