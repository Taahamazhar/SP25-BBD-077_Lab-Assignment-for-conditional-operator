# Check if number is positive, negative, or zero
num = float(input("Enter a number: "))
print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")


# Check if a year is a leap year
year = int(input("Enter a year: "))
print(f"{year} is a Leap Year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else f"{year} is not a Leap Year")


# Simple calculator
num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
print(f"Result: {num1 + num2}" if op == '+' else f"Result: {num1 - num2}" if op == '-' else f"Result: {num1 * num2}" if op == '*' else f"Result: {num1 / num2}" if op == '/' and num2 != 0 else "Invalid Operation")



# Student grading system
marks = int(input("Enter student's marks: "))
print("Grade: A" if marks >= 85 else "Grade: B" if marks >= 70 else "Grade: C" if marks >= 50 else "Grade: F")
