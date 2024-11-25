
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
rect_area = lambda l, b: l * b
rect_perimeter = lambda l, b: 2 * (l + b)
print("Area of the rectangle:", rect_area(length, breadth))
print("Perimeter of the rectangle:", rect_perimeter(length, breadth))
print("Square")
side = int(input("Enter the side length of the square: "))
square_area = lambda a: a * a
square_perimeter = lambda a: 4 * a
print("Area of the square:", square_area(side))
print("Perimeter of the square:", square_perimeter(side))
