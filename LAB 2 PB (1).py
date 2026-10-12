#1#
# num = int(input("Enter a number: "))

# if num % 5 == 0:
#     print("Hi")
# else:
#     print("Bye")

#2#
# X = float(input("Enter the first parallel side (X): "))
# Y = float(input("Enter the second parallel side (Y): "))
# H = float(input("Enter the height (H): "))

# area = ((X + Y) * H) / 2

# print("Area of the trapezoid =", area)

#3#
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in metres: "))

# bmi = weight / (height ** 2)

# print("BMI =", round(bmi, 2))

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal weight")
# elif bmi < 30:
#     print("Slightly overweight")
# elif bmi < 35:
#     print("Obese")
# else:
#     print("Clinically obese")

#4#
# alphabet = input("Enter an alphabet: ")

# if alphabet in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Consonant")

#5#
# initial = 2.19e14
# final = 4.68e14

# growth = ((final - initial) / initial) * 100

# print("Percentage of bacterial growth =", round(growth), "%")

#6#
# months = int(input("Enter the number of months: "))

# years = months // 12
# remaining_months = months % 12

# print("Years =", years)
# print("Months =", remaining_months)

#7#
# color = input("Enter the color (Blue/Red): ").lower()
# mode = input("Enter the mode (Steady/Flashing): ").lower()

# if color == "blue" and mode == "steady":
#     print("Clear view.")
# elif color == "blue" and mode == "flashing":
#     print("Clouds due.")
# elif color == "red" and mode == "steady":
#     print("Rain ahead.")
# elif color == "red" and mode == "flashing":
#     print("Snow instead.")
# else:
#     print("Invalid input.")   

#8#
# costs = float(input("Enter the costs: "))
# revenue = float(input("Enter the revenue: "))

# if costs == revenue:
#     print("Break even")
# elif revenue > costs:
#     profit = revenue - costs
#     print("Profit =", profit)
# else:
#     loss = costs - revenue
#     print("Loss =", loss)
    
#9#
# widgets = int(input("Enter the number of widgets ordered: "))

# if widgets >= 100:
#     cost = widgets * 0.20
# else:
#     cost = widgets * 0.25

# print("Total cost = $", round(cost, 2))

#10#
# pounds = float(input("Enter the number of pounds of apples: "))
# cash = float(input("Enter the amount of cash tendered: $"))

# cost = pounds * 2.50

# if cash >= cost:
#     change = cash - cost
#     print(f"Change = ${change:.2f}")
# else:
#     owe = cost - cash
#     print(f"You owe ${owe:.2f} more.")

#11#
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b:
#     if a > c:
#         largest = a
#     else:
#         largest = c
# else:
#     if b > c:
#         largest = b
#     else:
#         largest = c

# print("Largest number =", largest)

#12#
# basic_salary = float(input("Enter the basic salary: "))

# HRA = 20 / 100 * basic_salary
# TA = 5 / 100 * basic_salary
# DA = 10 / 100 * basic_salary

# gross_salary = basic_salary + HRA + TA + DA

# print("HRA =", HRA)
# print("TA =", TA)
# print("DA =", DA)
# print("Gross Salary =", gross_salary)

#13#
# basic_salary = float(input("Enter the basic salary: "))

# HRA = 0.20 * basic_salary
# TA = 0.05 * basic_salary
# DA = 0.10 * basic_salary

# gross_salary = basic_salary + HRA + TA + DA

# if gross_salary < 300000:
#     tax_rate = 0
# elif gross_salary <= 1000000:
#     tax_rate = 10
# elif gross_salary <= 2500000:
#     tax_rate = 20
# else:
#     tax_rate = 30

# income_tax = (tax_rate / 100) * gross_salary

# print("Gross Salary =", gross_salary)
# print("Income Tax Slab =", tax_rate, "%")
# print("Income Tax =", income_tax)

#14#
# income = float(input("Enter taxable income: "))

# if income <= 20000:
#     tax = 0.02 * income

# elif income <= 50000:
#     tax = 400 + 0.025 * (income - 20000)

# else:
#     tax = 1150 + 0.035 * (income - 50000)

# print("Tax =", tax)
    