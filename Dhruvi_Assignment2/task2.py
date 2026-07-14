"""Task 2: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""
num= 1
for i in range(1, 51):
    num+= i
print("The sum of integers from 1 to 50 is:", num)