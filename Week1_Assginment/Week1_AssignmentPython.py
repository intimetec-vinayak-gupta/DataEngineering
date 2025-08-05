# Day 1 - Write a program to swap the values of two variables without using a temporary variable.
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a, b)

# We can also use direct b, a = a, b

# Day 1 - Write a program to check whether a given year is a leap year
year = int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Given Year is a Leap year")
elif year % 400 == 0:
    print("Given Year is a Leap year")
else:
    print("Given Year is not  a Leap year")

# Day 1 - Write a program that asks the user to input a password. Check if the password meets the criteria (e.g., minimum length, inclusion of numbers and special characters). 
password = input("Enter password: ")
minLength = 8
lengthCheck = len(password) >= minLength
hasNumber = False
hasSpecialCharacter = False

for char in password:
    if char.isdigit():
        hasNumber = True
    if char in "!@#$%&*":
        hasSpecialCharacter = True

if lengthCheck and hasNumber and hasSpecialCharacter:
    print("Password is valid")
else:
    print("Password is invalid")

# Day 1 - Write a program that prints the pyramid pattern using nested loops 
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Day 1 - Understand the basics of memory management in Python, such as how objects are allocated and deallocated 

# Day 2 - Write a Python program that counts the occurrences of each character in a given string. 
try:
    myString = input("Enter string: ")
    charCount = {}
    for ch in myString:
        if ch in charCount:
            charCount[ch] = charCount[ch] + 1
        else:
            charCount[ch] = 1
    print(charCount)
except Exception as e:
    print(f"Error: {e}")

# Day 2 - Write a program that initializes a list, appends an element, removes an element, checks for a specific element, and prints the modified list
try:
    myList = []
    myList.append(10)
    myList.append(20)
    myList.append(30)
    print(myList)
    myList.remove(20)
    print(myList)
    if 10 in myList:
        print("10 is in the list")
    else:
        print("10 is not present in the list")
    print(myList)
except Exception as e:
    print(f"Error: {e}")

# Day 2 - Write a script that filters a dictionary to include only key-value pairs where the key starts with the letter 'A.'
try:
    originalDict = {'apple': 5, 'banana': 8, 'avocado': 3, 'cherry': 12, 'apricot': 7}
    filteredDict = {}
    for key, value in originalDict.items():
        if key[0] == 'A' or key[0] == 'a':
            filteredDict[key] = value
        
    print(filteredDict)
except Exception as e:
    print(f"Error: {e}")

# Day 2 - Given a tuple representing the dimensions (length, width, height) of a rectangle, write a program to unpack the tuple and print the dimensions separately. 
try:
    rectangle = (10, 5, 3)
    length, width, height = rectangle
    print("Length:", length)
    print("Width:", width)
    print("Height:", height)
except Exception as e:
    print(f"Error: {e}")

# Day 2 - Develop a Python script that takes user input and writes it to a new text file
try:
    userInput = input("Enter text to write to file: ")
    with open("output.txt", "w") as file:
        file.write(userInput)
    print("Text written to output.txt")
except Exception as e:
    print(f"Error: {e}")

# Day 3 - Implement a recursive function to calculate the factorial of a given number. 
def factorial(n):
    try:
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except Exception as e:
        print(f"Error: {e}")
        return None

num = int(input("Enter number for factorial: "))
result = factorial(num)
print(result)

# Day 3 - Enhance the previous program to include try-except blocks for file-handling errors. 
try:
    fileName = input("Enter filename to write: ")
    content = input("Enter content: ")
    with open(fileName, "w") as file:
        file.write(content)
    print(f"Content written to {fileName}")
except FileNotFoundError:
    print("Error: File path not found")
except PermissionError:
    print("Error: Permission denied to write file")
except Exception as e:
    print(f"Unexpected error: {e}")

# Day 3 - Write a one-liner Python program that uses lambda, map, and apply to transform a list of integers, and numbers, by adding 10 to each element and then squaring the result. 
try:
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: (x + 10) ** 2, numbers))
    print(result)
except Exception as e:
    print(f"Error: {e}")

# Day 4 - Write a program to add two matrices.  
from numpy import *
try:
    matrix1 = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    print(matrix1 + matrix2)
        
except ValueError as e:
    print(f"Value Error: {e}")
except Exception as e:
    print(f"Error: {e}")

# Day 4 - Write a program that takes user input for age as a string, converts it to an integer, and checks if the user is eligible to vote. 
try:
    ageInString = input("Enter your age: ")
    age = int(ageInString)
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
except ValueError:
    print("Error: Please enter a valid number")
except Exception as e:
    print(f"Error: {e}")

# Day 4 - Write a Python program that prompts the user to enter their birthdate in the format "YYYY-MM-DD" and validates the birthdate format using a regular expression and calculates their age if the format is correct and "Invalid Format" otherwise 
import re
from datetime import datetime

try:
    birthdate = input("Enter birthdate (YYYY-MM-DD): ")
    
    if re.match(r'^\d{4}-\d{2}-\d{2}$', birthdate):
        dt = datetime.strptime(birthdate, "%Y-%m-%d")
        birthYear = dt.year
        birthMonth = dt.month
        birthDay = dt.day
        #birthYear, birthMonth, birthDay = map(int, birthdate.split('-'))
        birthDateObject = datetime(birthYear, birthMonth, birthDay)
        currentDate = datetime.now()
        age = currentDate.year - birthDateObject.year
        
        if currentDate.month < birthDateObject.month:
            age -= 1
        elif currentDate.month == birthDateObject.month and currentDate.day < birthDateObject.day:
            age -= 1
            
        print(f"Your age is: {age}")
    else:
        print("Invalid Format")
        
except ValueError:
    print("Invalid Format")
except Exception as e:
    print(f"Error: {e}")

# Day 4 - Write a Python program that reads a CSV file named "data.csv" containing information about students (columns: Name, Age, Grade). The program should read the CSV file, convert CSV into JSON format, and send the JSON data to a specific API endpoint using the requests library. 
