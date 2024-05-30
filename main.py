import math


class Circle:

    def __init__(self, radius: int = 0):
        self.radius = radius
        self.diameter = 0
        self.circumference = 0
        self.area = 0

    def calculate_diameter(self):
        self.diameter = 2 * self.radius
        return f'Diameter: {self.diameter}'

    def calculate_circumference(self):
        self.circumference = 2 * math.pi * self.radius
        return f'Circumference: {self.circumference}'

    def calculate_area(self):
        self.area = math.pi * self.radius ** 2
        return f'Area: {self.area}'

    def grow(self):
        print()
        print('Stand by while your circle magically grows...')
        self.radius *= 2

    def get_radius(self):
        while True:
            self.radius = float(input('Enter a radius: '))
            if self.radius <= 0:
                print('Radius must be positive. Try again')
            else:
                self.radius = round(self.radius, 2)
                break


print('Welcome to the Circle Tester!')
circle1 = Circle()
circle1.get_radius()

print(circle1.calculate_diameter())
print(circle1.calculate_circumference())
print(circle1.calculate_area())


while True:
    grow = str(input('Would you like your circle to grow? (y/n) >> ')).lower()
    if grow != 'y':
        print('Goodbye')
        quit()
    else:
        circle1.grow()
        print(circle1.calculate_diameter())
        print(circle1.calculate_circumference())
        print(circle1.calculate_area())


# class Validator:
# Create a class named Validator and use its methods to validate the data in this application.