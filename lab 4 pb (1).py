#1#
# salary = float(input("Enter salary: "))
# years = int(input("Enter years of service: "))

# if salary < 0 or years < 0:
#     print("Invalid input")
# else:
#     if years > 5:
#         bonus = salary * 0.05
#     else:
#         bonus = 0

#     print("Net bonus amount =", bonus)

#2#
# password = input("Enter password: ")

# if password == "s3cr3t!P@ssw0rd":
#     print("Welcome")
# else:
#     print("Wrong password!")
    
#3#
# shape = input("Enter shape (square/rectangle/circle/triangle): ").lower()

# if shape == "square":
#     side = float(input("Enter side: "))

#     if side <= 0:
#         print("Invalid input")
#     else:
#         area = side * side
#         print(f"Area = {area:.3f}")

# elif shape == "rectangle":
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))

#     if length <= 0 or width <= 0:
#         print("Invalid input")
#     else:
#         area = length * width
#         print(f"Area = {area:.3f}")

# elif shape == "circle":
#     radius = float(input("Enter radius: "))

#     if radius <= 0:
#         print("Invalid input")
#     else:
#         area = 3.141592653589793 * radius * radius
#         print(f"Area = {area:.3f}")

# elif shape == "triangle":
#     base = float(input("Enter base: "))
#     height = float(input("Enter height: "))

#     if base <= 0 or height <= 0:
#         print("Invalid input")
#     else:
#         area = 0.5 * base * height
#         print(f"Area = {area:.3f}")

# else:
#     print("Invalid shape")
    
#4#
# hours = int(input("Enter hours: "))
# minutes = int(input("Enter minutes: "))

# if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
#     print("Invalid time")
# else:
#     total_minutes = hours * 60 + minutes + 15

#     new_hours = (total_minutes // 60) % 24
#     new_minutes = total_minutes % 60

#     print(f"{new_hours}:{new_minutes:02d}")

#5#
# distance = float(input("Enter distance in km: "))
# period = input("Enter period (day/night): ").lower()

# if distance <= 0:
#     print("Invalid distance")
# elif period not in ["day", "night"]:
#     print("Invalid period")
# else:
#     # Taxi price
#     if period == "day":
#         taxi_price = 33.58 + distance * 37.89
#     else:
#         taxi_price = 33.58 + distance * 43.17

#     # Bus price
#     if distance >= 20:
#         bus_price = distance * 4.32
#     else:
#         bus_price = float("inf")

#     # Train price
#     if distance >= 100:
#         train_price = distance * 2.88
#     else:
#         train_price = float("inf")

#6#
# holidays = int(input("Enter number of holidays: "))

# if holidays < 0 or holidays > 365:
#     print("Invalid number of holidays")
# else:
#     workdays = 365 - holidays

#     total_play_time = (workdays * 63) + (holidays * 127)
#     norm = 30000

#     difference = abs(norm - total_play_time)

#     if total_play_time <= norm:
#         print("Tom will sleep well.")
#         print("Difference from norm =", difference, "minutes")
#     else:
#         print("Tom will not sleep well.")
#         print("Difference from norm =", difference, "minutes")
    
#7#
# budget = float(input("Enter budget in BGN: "))
# season = input("Enter season (summer/winter): ").lower()

# if budget <= 0:
#     print("Invalid budget")
# elif season not in ["summer", "winter"]:
#     print("Invalid season")
# else:
#     if budget <= 100:
#         destination = "Bulgaria"

#         if season == "summer":
#             percentage = 0.30
#             place = "camping"
#         else:
#             percentage = 0.70
#             place = "hotel"

#     elif budget <= 1000:
#         destination = "Balkans"

#         if season == "summer":
#             percentage = 0.40
#             place = "camping"
#         else:
#             percentage = 0.80
#             place = "hotel"

#     else:
#         destination = "Europe"
#         percentage = 0.90
#         place = "hotel"

#     amount = budget * percentage

#     print("Destination:", destination)
#     print("Accommodation:", place)
#     print(f"Money spent: {amount:.2f} BGN")

#8#
# for number in range(1,1001):
#     if number % 10 == 6:
#         print(number)
        
#9#
# n = int(input("Enter n: "))
 
# if n <= 0:
#     print("Invalid value of n")
# else:
#     total = 0 
#     for i in range(n):
#         number = int(input(f"Enter integer {i + 1}: "))
#         total += number

#     print("Sum =", total)

#10#
# N = int(input("Enter a positive integer: "))

# if N <= 0:
#     print("Invalid input")
# else:
#     for i in range(1, 21):
#         print(f"{N} x {i} = {N * i}")
