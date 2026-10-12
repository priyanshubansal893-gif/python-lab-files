# x1 = int(input(" Enter x coordinate of centre "))
# y1 = int(input(" Enter y coordinate of centre "))
# r = int(input("Enter Radius"))
# if r <=0:
#    print("Invalid input: Radius must be greater than 0") 
# else:
#     x2 = int(input("Enter x coordinate of point "))
#     y2 = int(input("Enter y coordinate of point "))
# distance_squared = (x2-x1)**2 + (y2-y1)** 2
# radius_squared = r** 2
# if distance_squared < radius_squared:
#     print("The point lies inside the circle.")
# elif distance_squared == radius_squared:
#     print("The point lies on boundary of circle")
# else:
#     print("the point lies outside the circle.")
    
    
#2# 
# import math
# s = float(input("Enter the side of the pentagon: "))
# area = (5 * s**2) / (4 * math.tan(math.pi / 5))
# print("Area of the pentagon =", area)

# #3#
# # Input three angles
# a = float(input("Enter the first angle: "))
# b = float(input("Enter the second angle: "))
# c = float(input("Enter the third angle: "))

# # Check whether the angles can form a triangle
# if a <= 0 or b <= 0 or c <= 0 or a + b + c != 180:
#     print("The angles cannot form a triangle.")
# else:
#     # Classify the triangle
#     if a < 90 and b < 90 and c < 90:
#         print("The triangle is acute-angled.")
#     elif a == 90 or b == 90 or c == 90:
#         print("The triangle is right-angled.")
#     else:
#         print("The triangle is obtuse-angled.")

#4#
# num = int(input("Enter a 4-digit number: "))

# first_two = num // 100
# last_two = num % 100

# sum_first = (first_two // 10) + (first_two % 10)
# sum_last = (last_two // 10) + (last_two % 10)

# print("Sum of first two digits:", sum_first)
# print("Sum of last two digits:", sum_last)

# if sum_first == sum_last:
#     print("Both sums are equal.")
# else:
#     print("Both sums are not equal.")
    
#5#
# num = int(input("Enter a 5-digit number: "))

# d1 = num // 10000
# d2 = (num // 1000) % 10
# d3 = (num // 100) % 10
# d4 = (num // 10) % 10
# d5 = num % 10

# largest = d1
# position = 1

# if d2 > largest:
#     largest = d2
#     position = 2

# if d3 > largest:
#     largest = d3
#     position = 3

# if d4 > largest:
#     largest = d4
#     position = 4

# if d5 > largest:
#     largest = d5
#     position = 5

# print("Largest digit:", largest)
# print("Position from left:", position) 


#6#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# a = a + b + c
# b = a - b - c
# c = a - b - c
# a = a - b - c

# print("After rotation:")
# print("a =", a)
# print("b =", b)
# print("c =", c)             

#7#
# num = int(input("Enter a 3-digit number: "))

# a = num // 100
# b = (num // 10) % 10
# c = num % 10

# sum_digits = a + b + c

# if num % sum_digits == 0:
#     print("Harshad number")
# else:
#     print("Not a Harshad number")

#8#
# V = float(input("Enter the initial quantity of water (litres): "))
# N = int(input("Enter the number of days: "))

# if V < 0 or N < 0:
#     print("Invalid input")
# else:
#     quantity = 200 + (V - 200) * (0.95 ** N)
#     print("Quantity of water after", N, "days =", quantity, "litres")
    
#9#
# a1 = float(input("Enter a1: "))
# b1 = float(input("Enter b1: "))
# c1 = float(input("Enter c1: "))

# a2 = float(input("Enter a2: "))
# b2 = float(input("Enter b2: "))
# c2 = float(input("Enter c2: "))

# D = a1 * b2 - a2 * b1

# if a1 == 0 and b1 == 0:
#     print("Invalid first line")
# elif a2 == 0 and b2 == 0:
#     print("Invalid second line")
# elif D != 0:
#     x = (c1 * b2 - c2 * b1) / D
#     y = (a1 * c2 - a2 * c1) / D

#     print("Point of intersection:")
#     print("x =", format(x, ".2f"))
#     print("y =", format(y, ".2f"))
# elif a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
#     print("The lines are coincident")
# else:
#     print("The lines are parallel")
    
