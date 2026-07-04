# This is the start of python revision from the start in order to perfect my skills in python programming language

# DAY- 1
#str= "hello"
#print(str)
# boolean- True or False
# /n to change the line
# """ multi line comment """
#  when we assign a value to a variable it is called literal
# variable name should not start with a number
# variable is a container that holds data in it
# primitive datatypes- int, float, str, bool, none
# type() function is used to check the datatype of a variable
# none is no value or null value
# + is used for addition and concatenation
#len () function is used to check the length of a string
# [] is used to access the index of a string
# language + str("version")
#python3.13


# DAY- 2
# +, =, -, *, /, //, %, ** are arithmetic operators
# airthmetic operators are used to perform mathematical operations on numbers
# division operator (/) returns a float value
# floor division operator (//) returns an integer value
# modulus operator (%) returns the remainder of a division operation
# exponent operator (**) returns the power of a number
# Assignment operators are used to assign values to variables
# =, +=, -=, *=, /=, //=, %=, **= are assignment operators
# comparison operators are used to compare two values and return a boolean value
# ==, !=, >, <, >=, <= are comparison operators
# Logical operators are used to combine multiple boolean expressions and return a boolean value
# and, or, not are logical operators
# not operator is used to reverse the boolean value of an expression
# not True = False, not False = True
# precedence of operators is used to determine the order in which operators are evaluated in an expression
# 5 + 10 * 6= 65
# precedence order- (),**, *, /, //, %, +, -, =, +=, -=, *=, /=, //=, %=, **=, ==, !=, >, <, >=, <=, and, or, not
# associativity of operators is used to determine the order in which operators of the same precedence are evaluated in an expression
# left to right associativity- +, -, *, /, //, %, **, =
# classification of operators based on the number of operands they operate on- unary, binary, ternary
# - is a unary as well as binary operator
# sep= is used to separate the values in a print statement
# sep(#)- print("hello", "world", sep="#")= hello#world
# input() function is used to take input from the user
# input() function always returns a string value
# numeric functions- int(), float(), complex() are used to convert a string value to a numeric value
#max() function is used to find the maximum value among the given values
# min() function is used to find the minimum value among the given values
# abs() function is used to find the absolute value of a number
# pow() function is used to find the power of a number  

""" Coding execise- 1

area_of_ triangle when length of the sides is known= a, b, c
s= ( a + b + c ) / 2
area= (s * (s - a) * (s - b) * (s - c)) ** 0.5
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
print("The area of the triangle is:", round(area, 2))
ans= 26.83

simple_interest= (p * r * t) / 100
p= float(input("Enter the principal amount: "))
r= float(input("Enter the rate of interest: "))
t= float(input("Enter the time in years: "))
print("The simple interest is:", round(simple_interest, 2))

compound_interest= p * (1 + r / 100) ** t - p
p= float(input("Enter the principal amount: "))
r= float(input("Enter the rate of interest: "))
t= float(input("Enter the time in years: "))
print("The compound interest is:", round(compound_interest, 2))



"""
# len() function is used to find the length of a string
# start: starting index of the substring to be searched. Default is 0.
# end: ending index of the substring to be searched. Default is the length of the string.
#[-1] is used to access the last index of a string
# fstring is used to format a string by embedding expressions inside string literals
#fstring= f"Hello, {first_name} {last_name}! Welcome to the Python program."
# escape sequences are used to represent special characters in a string
# \n= new line
# \t= tab
# apostrophe= \'
# backslash= \\ to represent a backslash in a string
# comparison of strings is done using comparison operators
# strip() function is used to remove the leading and trailing whitespaces from a string
#replace() function is used to replace a substring with another substring in a string
# _old= substring to be replaced
# _new= substring to replace with
# replace(_old, _new)= string.replace(_old, _new)
# count() function is used to count the number of occurrences of a substring in a string
# string.count(substring)
# upper() function is used to convert a string to uppercase
# lower() function is used to convert a string to lowercase
# capitalize() function is used to convert the first character of a string to uppercase and the rest to lowercase
# title() function is used to convert the first character of each word in a string to uppercase and the rest to lowercase
# startswith() function is used to check if a string starts with a specified substring
# PYTHON IS CASE SENSITIVE LANGUAGE
# endswith() function is used to check if a string ends with a specified substring
