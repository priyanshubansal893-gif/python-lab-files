#1#
# n = input("Enter a string: ")
# rev = " "
# for i in range(len(n) -1,-1,-1):
#     rev = rev + n[i]
# print("Reversed string:", rev)

#2#
# sentence = input("Enter a sentence: ")
# words = sentence.strip()
# if words:
#     print("Length of the last word:", len(words[-1]))
# else:
#     print("Length of the last word: 0")
    
   
#3#
# s = input("Enter a sentence: ")
# w=input("Enter a word: ")
# count=0
# for i in range(len(s)-len(w)+1):
#     match=True
#     for j in range(len(w)):
#         if s[i+j]!=w[j]:
#             match=False
#             break
#     if match:
#         count += 1
# if count>0:
#     print("Word found")
# else:
#     print("Word not found")
# print(f"Count: {count}")

#4#
# s = input("Enter sentence ")
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# count = 0
# for ch in alphabet:
#     if ch in s.lower():
#         count = count + 1
# if count == 26:
#     print("Pangram")
# else:
#     print("Not a pangram")

#5#
# s = input("Enter a string: ")
# e= int(input("shift:"))
# total=" "
# a="abcdefghijklmnopqrstuvwxyz"
# for i in s:
#     z = a.index(i)
#     total= total+ a[(z+e)%26]
# print(total)

#6#
counts = [0, 0, 0, 0, 0]  
total_numbers = 0
print("Enter numbers between 1 and 10 :")
while True:
    num = int(input())
    if num == -1:
        break
    if 1 <= num <= 2:
        counts[0] += 1
    elif 3 <= num <= 4:
        counts[1] += 1
    elif 5 <= num <= 6:
        counts[2] += 1
    elif 7 <= num <= 8:
        counts[3] += 1
    elif 9 <= num <= 10:
        counts[4] += 1
    total_numbers += 1
ranges = ["1-2", "3-4", "5-6", "7-8", "9-10"]
for i in range(5):
    percentage = (counts[i] / total_numbers * 100) if total_numbers > 0 else 0.00
    hashes = "#" * counts[i]
    print(f"{ranges[i]}:{hashes}{percentage:.2f}%")


#7#
# s = input("Enter a string: ")
# is_palindrome = True
# n = len(s)
# for i in range(n // 2):
#     if s[i] != s[n - 1 - i]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#8#
# n = int(input("How many numbers do you want to enter? "))
# numbers = []
# for i in range(n):
#     num = int(input("Enter number: "))
#     numbers = numbers + [num]
# total_sum = 0
# product = 1
# smallest = numbers[0]
# for x in numbers:
#     total_sum += x
#     product *= x
#     if x < smallest:
#       smallest = x
# print("Sum of numbers:", total_sum)
# print("Product of numbers:", product)
# print("Smallest number:", smallest)


# #9
# nums = [int(x) for x in input("Enter integers separated by space: ").split()]
# n = len(nums)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if nums[j] < nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print("List sorted in descending order:", nums)


# #10
# sequence = input("Enter a hyphen-separated sequence of words: ")
# words = sequence.split("-")
# n = len(words)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if words[j] > words[j + 1]:
#             words[j], words[j + 1] = words[j + 1], words[j]
# sorted_sequence = "-".join(words)
# print("Expected Result:", sorted_sequence)


# #11
# p = input("Enter a paragraph: ")
# digits = 0
# alphabets = 0
# special = 0
# upper = 0
# lower = 0
# for char in p:
#     if char.isdigit():
#         digits += 1
#     elif char.isalpha():
#         alphabets += 1
#         if char.isupper():
#             upper += 1
#         else:
#             lower += 1
#     else:
#         special += 1
# print(f"Alphabets: {alphabets} (Uppercase: {upper}, Lowercase: {lower})")
# print(f"Digits: {digits}")
# print(f"Special characters: {special}")


# #12
# s = input("Enter a string: ")
# result = ""
# for char in s:
#     if char not in result:
#         result += char

# print("Without duplicates:", result)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
