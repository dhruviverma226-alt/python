# tuples are  immutable sequences, typically used to store collections of heterogeneous data.
# They are defined by enclosing the elements in parentheses `()`, and can contain any number of items, including other tuples. 
# Tuples support indexing, slicing, and iteration, but unlike lists, they cannot be modified after creation.
# t1 = (1, 2, 3, "hello", True)
# a list can be present inside a tuple,
# but a tuple cannot be present inside a list because 
# lists are mutable and tuples are immutable.
# accessing elements in a tuple is done using indexing, similar to lists.
# [-1] is used to access the last element.
# type() - 'tuple' is in small letters.
# in order to convert tuple into list :
# list cannot be changed into a tuple 
# because tuples are immutable, 
# but a tuple can be converted into a list using the `list()` function.

""" example: 
fruits= ("apple", "banana", "cherry")
print(fruits, type(fruits))
fruits = list(fruits)
print(fruits, type(fruits))
"""
# operations on tuples
# concatenation of tuples: '+' is used to combine two or more tuples together.
# print(tuple1 + tuple2)
# repetition of tuples: '*' is used to repeat a tuple multiple times.
# print(tuple2 * 3)
# membership testing: 'in' is used to check if a specified value exists in the tuple. 
# It returns True if the value is found, otherwise False.
# not in is used to check if a specified value does not exist in the tuple.
# count method returns the number of occurrences of a specified value in the tuple.
# tuple.count(value)
# index method returns the index of the first occurrence of a specified value in the tuple.
# tuple.index(value)
# min function is used to find the minimum value in a tuple of numbers.
# min(tuple)
# max function is used to find the maximum value in a tuple of numbers.
# max(tuple)
# sum function is used to calculate the sum of all elements in a tuple of numbers.
# sum(tuple)

# mutability is the ability of a value or data to be able to changed.
# immutability is the inability of a value or data to be able to changed.
# tuples and strings are immutable.
# strings do not change after they are created
# append cannot be used in tuples
# id gives memory address of the object in python.
# list can be modified.



