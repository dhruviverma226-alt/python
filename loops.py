# loops is the repetition of a program to perform an action multiple times without writing it again and again.
# it helps in automation.
# types of loops: for loop and while loop
# for loop: it is an iterator which steps throught the items of a collection
# (lists, tuples, sets, dict, str), and executes a block of code repeatedly
#  for a number of times equal to the items/ elements of that collection
"""
for var in sequence:
    statement1
    statement2
    ...
    statementn
"""
# marks= [85.5, 81.0, 86.0, 83.5]
# print(marks[0])
# for m in marks:
#     print(m)
# loop runs through the length of the list and prints each element of the list

# for loop in a string
"""s1= "hello world"
for char in s1:
    print(char)"""
# loop runs through the length of the string and prints each character of the string

# for loop in a dictionary
"""emp= {"id":1001, "name": "dhruvi"}
for key in emp:
    print(key, emp[key])"""
# loop runs through the length of the dictionary and prints each key and value of the dictionary
# range function: it generates a sequence of numbers
# syntax: range(start, stop, step)
# start: the starting point of the sequence (default is 0)
# stop: the stopping point of the sequence (default is infinite)
"""for i in range(10, 0, -1):
    print(i)
print("happy new year")
"""