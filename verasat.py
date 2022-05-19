from turtle import title, width
import arcade


class Circle(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.r = float(input("enter radius: "))
        self.area = (2*3.14)*self.r
        self.perimeter = (self.r*self.r)*3.14
        print("area of circle:", self.area, "  ",
              "perimeter of circle:", self.perimeter)


class Rectangle(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = float(input("enter width: "))
        self.height = float(input("enter height: "))
        self.area = (self.width + self.height)*2
        self.perimeter = (self.width*self.height)
        print("area of rectangle:", self.area, "  ",
              "perimeter of rectangle:", self.perimeter)


class game(arcade.Window):
    def __init__(self):
        self.circle = Circle()
        self.rectangle = Rectangle()


game()
