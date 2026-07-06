# if statement : it is a simple decision making statement. 
# it executes only if the condition is true
# indentation is four spaces by default.
# example:
# age= float(input("enter age: "))

# if age>=18:
#     print("you can vote.")
# print("statement block completed.")

# if-else: it allows program to execute one block of code if the condision is true, and a different code of code if the condition is false.
# it is like if statement but it provides alternative path.
# example:
""" 
if condition:
    code executes if true
else: 
    code executes if false

"""
# if-elif-else: when you have more than two possible outcomes, you use elif statement.
# multiple conditions:
# example:
"""
marks= float(input("Enter your marks"))
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks <80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
else:
    print("F")
"""
# Nested if statements: A nested if statement is an if statement inside another if statement.
# It is used to check a second condition only if the first condition is true.
# example:
"""
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
"""
# ternary operators: A ternary operator is a shorthand way of writing an if-else statement.
# It is used to assign a value to a variable based on a condition.
# example: 
"""
true-expression if condition else false-expression
print("even") if num %= 2==0 else print("odd")

"""