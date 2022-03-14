from src.Square import Square

square = Square(10)
print(square.name)
print('square.area=', square.area)
square2 = Square(1)
print('square2.area=', square2.area)
square2.add_area(square)
