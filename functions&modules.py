# built in functions- already present functions developed by developers that is present when we download python!!
# user-defined functions- functions that we create ourselves!!
# functions are used to perform a specific task!!
# syntax of function- def function_name(parameters):
# function_name is the name of the function
# parameters are the values that we pass to the function
# def is used to define a function
# parameters are optional
# parameters are used to pass values to the function

"""example:
def greeting(name):
    print(f"Hello {name}")
    print("its a beautiful day")

greeting("Dhruvi")"""

"""def even_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
even_odd(10)"""
# returning values- "none" is returned if the functions stores the value

"""def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_odd(10))
"""
# types of argument
# default argument, Keyword argument, *args (allows variable-length) argument
# *args- allows multiple values, the values are stored in a tuple. 
# *args is just a standard way. any variable can be used instead of args such as *nums
# **kwargs is the variable length keyword argument. it stores the values in a dictionary.
"""def func(**kwargs):
    print(kwargs)
func()""" # type is dictionary.
# arguments do not come after **kwargs, first arguments are written and that last **kwargs is written.
# def func()
"""
    this is the doctring
    we can write whatever the function does here
    :return: none
    """
""" help function- it is used to get the documentation of the function. help()
it only works if the doctring is the first thing in the function"""

# recursion- calling a function inside itself
# recursive function- a function that calls itself
# example: 
# factorial of a number- 5! = 5*4*3*2*1 = 120
# factorial of 0 is 1
# factorial of 1 is 1

"""def fac_rec(num):
    if num == 1:
        return 1
    else:
       factorial = num * fac_rec(num-1)
       return factorial

print(fac_rec(4)) """   

"""
n= 1 # GLOBAL VARIABLE- CAN BE ACCESSED FROM ANYWHERE

def fn():
    n= 5 # LOCAL VARIABLE- CAN ONLY BE ACCESSED INSIDE THE FUNCTION
    print(n)
fn()

print(n)
ASSIGN A DIFFERENT VARIABLE FROM OUTSIDE TO INSIDE- global n
local variable is preferred at higher place than the global variable


"""
# In python, you can pass a function as argument of another function.

# lambda- it is an anonymous function.
# syntax- lambda argument : expression
"""func= lambda a : a+ 1 # two args- func = lambda a,b : a + b # res = func(2, 5)
res= func(2)
print (res)"""

# filter and map function in lambda
# filters from the list.
# filter(lambda x: True if x % 2!= 0 else False, seq) for any sequence given.
# map function keeps whatever output we get. on each the elements.

# .py file is a module.
# built-in modules and user-defined modules
# built in is already present in python. eg. math module, random module, etc.,
# syntax: import module_name, from module_name import func1, func2, etc,.
"""import math
num = 100
output = math.sqrt(num)
print(f"Square root of {num} is {output}")
"""
"""import math
from math import pi
radius = 5
area= math.pi * (radius ** 2)
print(area)"""

# syntax to create an alias for the module that is imported: import module_name as alias_name
# User-defined modules: made using the .py 

# __name__ variable (revisit the video.. I'm tired)

