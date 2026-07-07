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
marks= [85.5, 81.0, 86.0, 83.5]
print(marks[0])
for m in marks:
    print(m)
    