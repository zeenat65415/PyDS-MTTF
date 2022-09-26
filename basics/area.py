#area oof rectangle
length=input("Enter length of a rectangle=>")
breadth=input("Enter breadth of a rectangle=>")
length=int(length)
breadth=int(breadth)
area=length*breadth
print("Area of rectangle is:",area)

#area of square
side=float(input("Enter side of a square=>"))
area=side**2
print("Area of square is:",area)#comma separation
print(f"Area of square is:{area}")#f-string

#area of circle
radius=float(input("Enter radius of a circle=>"))
area=3.14*radius**2
print(f"Area of circle is:{area}" )