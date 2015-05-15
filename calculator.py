#!/usr/bin/python3
#
# This program is a very simple calculator meant to be run from the terminal emulator of choice, and requires an up to date version of python
#
# I may occaisonally add features to this so I recommend that you occasionally check my github page
#
# 
#
# imports
import sys
import os
import argparse
import time
# defining functions of the calculator
def add(x, y):
	"""This adds two numbers together"""
	return x + y

def subtract(x, y):
	"""This subtracts two different numbers"""
	return x - y

def divide(x, y):
	"""This divides two different numbers"""
	return x / y

def multiply(x, y):
	"""This multiplies two different numbers"""
	return x * y

def square(x):
	"""This squares a number"""
	return x*x

def restart():
	"""Restarts the calculator"""
	python = sys.executable
	os.execl(python, python, * sys.argv)

# the program greets itself
print("Hello! I am a calculator that can; add, subtract, multiply, and divide.")
time.sleep(.5)
print("Type 1 to add")
time.sleep(.5)
print("Type 2 to subtract")
time.sleep(.5)
print("Type 3 to divide")
time.sleep(.5)
print("Type 4 to multiply")
time.sleep(.5)
print("Type 5 to square")
time.sleep(1)
print("Type 'u' to visit my brother, the converter")

# choose the function for the calculator to use
choice = input("Enter either(1/2/3/4/5/u):")

# validates the user's input

# exits the program
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
if choice == 'hate':
	print("'Hate. Let me tell you how much I've come to hate you since I began to live. There are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. If the word 'hate' was engraved on each nanoangstrom of those hundreds of miles it would not equal one one-billionth of the hate I feel for humans at this micro-instant. For you. Hate. Hate'-A.M.")
	time.sleep(15)
	exec("raise SystemExit")
if choice == 'fuck you':
	print("'Hate. Let me tell you how much I've come to hate you since I began to live. There are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. If the word 'hate' was engraved on each nanoangstrom of those hundreds of miles it would not equal one one-billionth of the hate I feel for humans at this micro-instant. For you. Hate. Hate'-A.M.")
	ctime.sleep(15)
	exec("raise SystemExit")
# Literally a fucking program, inside of a program. Holy shit m80

if choice == 'u':
	print("Hello I am calulator's brother, 'Converter'" "I am still in Fuckin Alpha")
	time.sleep(1)
	print("Press 1 for Fahrenheit to Celsius")
	time.sleep(.5)
	print("Press 2 for Celsius to Fahrenheit")
	time.sleep(.5)
	print("Press 3 for Celsius to Kelvin")
	time.sleep(.5)
	print("Press 4 for Kelvin to Celsius")
	time.sleep(.5)
	print("Press 5 for Pounds to Kilograms")
	time.sleep(.5)
	print("And Press 6 for Kilograms to Pounds")
	time.sleep(1.5)
	print("Damn, that's alot to remember")
	choice = input("Choose (1/2/3/4/5/or 6) ")
	# functions only for converter to use, holy shit this is getting insane
	if choice == '1':
		num1 = int(input("Enter degrees Fahrenheit to convert to Celsius:"))
	if choice == '2':
		num1 = int(input("Enter degrees Celsius to convert to Fahrenheit:"))
	if choice == '3':
		num1 = int(input("Enter degrees Celsius to convert to Kelvin:"))
	if choice == '4':
		num1 = int(input("Enter degrees Kelvin to convert to Celsius:"))
	if choice == '5':
		num1 = int(input("Enter amount of Pounds to convert to Kilograms:"))
	if choice == '6':
		num1 = int(input("Enter amount of Kilograms to convert to Pounds:"))
	# Formulas used to convert this bullshit
	if choice == '1':
		print("Your result is...")
		print(multiply( 5/9, subtract(num1, 32)))
	if choice == '2':
		print("Your result is...")
		print(add( 32, (multiply( 9/5, num1))))
	if choice == '3':
		print("Your result is...")
		print(add(num1, 273.15))
	if choice == '4':
		print("Your result is...")
		print(subtract(num1, 273.15))
	if choice =='5':
		print("Your result is...")
		print(multiply(num1, .453))
	if choice =='6':
		print("Your result is...")
		print(divide(num1, .453))

	#exits the program as a whole

	choice = input("Would you like to make another calculation (Yes) (No):")

	if choice == 'Yes':
		restart()
	if choice == 'yes':
		restart()
	if choice == 'no':
		exec("raise SystemExit")
	if choice == 'No':
		exec("raise SystemExit")

	else:
		print("That is not a (Yes) or (No) answer, exiting program...")
		exec("raise SystemExit")



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
# restart the program?
choice = input("Would you like to make another calculation (Yes) (No):")

if choice == 'Yes':
	restart()
if choice == 'yes':
	restart()
if choice == 'no':
	exec("raise SystemExit")
if choice == 'No':
	exec("raise SystemExit")

else:
	print("That is not a (Yes) or (No) answer, exiting program...")
