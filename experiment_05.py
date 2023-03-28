# Write simple programs to calculate the area and perimeter of the square, 
# and the volume & perimeter of the cone.

# Area and Perimeter of Square
side = int(input("Enter length of side of Square: "))
area = side**2
perimeter = 4*side
print(f"Area of a Square: {area}, Perimeter of a Square: {perimeter}")

# volume & perimeter of the cone
pi = 3.1415
radius, height = [int(x) for x in input("Enter Radius & Height of Cone: ").split(",")]
volume = (pi*radius*radius*height)*(1/3)
perimeter = 2*pi*radius
print(f"Volume of a Cone: {volume}, Perimeter of a Cone: {perimeter}")