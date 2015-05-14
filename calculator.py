#/bin/env python
#
# This program is a very simple calculator meant to be run from the terminal emulator of choice, and requires an up to date version of python
#
# I may occaisonally add features to this so I recommend that you occasionally check my github page
#
# defining functions of the calculator
def add(x, y, z):
	"""This adds three numbers together"""
	return x + y + z

def subtract(x, y, z):
	"""This subtracts three different numbers"""
	return x - y - z

def divide(x, y):
	"""This divides two different numbers"""
	return x / y

def multiply(x, y):
	"""This multiplies two different numbers"""
	return x * y

def square(x):
	"""This squares a number"""
	return x*x

# the program greets itself
print("Hello! I am a calculator that can; add, subtract, multiply, and divide.")
print("Type 1 to add")
print("Type 2 to subtract")
print("Type 3 to divide")
print("Type 4 to multiply")
print("Type 5 to square")

# choose the function for the calculator to use
choice = input("Enter either(1/2/3/4) or (exit):")

#exits the program
if choice == 'exit':
	exec("raise SystemExit")

# input the numbers to calculate

if choice == '1':
	num1 = int(input("Enter your first number:"))
	num2 = int(input("Enter your second number:"))
	num3 = int(input("Enter your third number:"))
if choice == '2':
	num1 = int(input("Enter your first number:"))
	num2 = int(input("Enter your second number:"))
	num3 = int(input("Enter your third number:"))
if choice == '3':
	num1 = int(input("Enter your first number:"))
	num2 = int(input("Enter your second number:"))
if choice == '4':
	num1 = int(input("Enter your first number:"))
	num2 = int(input("Enter your second number:"))
if choice == '5':
	num1 = int(input("Enter the number to square:"))

# calculating functions
if choice == '1':
	print("Your result is...")
	print(num1,"+",num2,"+",num3,"=", add(num1, num2, num3))

elif choice == '2':
	print("Your result is...")
	print(num1,"-",num2,"-",num3,"=", subtract(num1, num2, num3))

elif choice == '3':
	print("Your result is...")
	print(num1,"/",num2,"=", divide(num1, num2))

elif choice == '4':
	print("Your result is...")
	print(num1,"*",num2,"=", multiply(num1, num2))

elif choice == '5':
	print("Your result is...")
	print(num1,"*",num1,"=", multiply(num1, num1))
# if someone done goofed
if choice == 'b':
	print("ERROR: TRY AGAIN")
