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
"""
profits= [9, 11, 6, 10]
for index in range(len(profits)):
    q= index + 1
    print("profit of quarter", q, "is", profits[index])
"""
"""
# continue and break statements: 
for num in range(10):
    if num % 3 == 0:
        continue #skips whatever is written after this line
    print(num)
"""
"""
for num in range (1, 10):
    if num % 3 == 0:
        break # terminates the loop
    print(num)
"""

# while loop is used when the number of iterations is not known in advance
# while loop is used when the condition is checked before the loop starts
# while loop is used when the condition is checked after the loop ends
# syntax: while condition:
"""num = 1
while num < 5:
    num += 1
    print(num)"""

# infinite loop
"""while true:
    print("hello")
"""
# break statement
"""num = 1
while num < 5:
    num += 1
    if num == 3:
        break
    print(num)"""
"""import random
nums= [10,4,1,8,4,3]
print(random.choice(nums))"""

# random.shuffle - shuffles the list
# nested loops:

"""for i in range(3):
    for j in range(2):
        print(f"i={i}, j= {j}")"""

# start pattern
"""for i in range(1,6):
    for j in range(1, i+1):
        print('x', end=" ")
    print()"""

# exercise:
"""
write a program to simuate a roll of a dice
a dice has 6 faces with number 1 to 6 written on them
the program should random;y print a number between 1 to 6

"""
"""import random
print("let's start the dice game")
while True:
    choice= input("roll the dice by pressing 'ENTER' or 'q' to quit..  ")
    if choice =='q':
        print('Thanks for playing')
        break
    elif choice == '':
        number = random.randint(1, 6)   
        print(number)

    else: 
        print("invalid input")"""
#  count all the countries which are starting with 'I'[
"""countries= ["India", "United States", "Australia", "Ireland", "Shri lanka", "Iceland",
             "Cuba", "Iran", "Poland"]
counter= 0
for country in countries:
    if country[0] == 'I':
        counter += 1
print(counter)""" ##1

# using country.startswith('I')
# using empty output list and then appending the list
# output.append(country)
# we have the following dictionary containing details:
"""user= {"user_name" : "myuser",
      "password" : "test@123",
      "email" : "myemail@gmail.com",
      "address":"ABC road, 111111",
      "country" : "Australia"

}
sensitive_info = ["password", "address", "phone"]
for i in sensitive_info:
    if i in user:
        print(f"DELETED => key: {i}, value: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present")
print(user)"""
# 
# 
# 
# 
# 
# 
# 
# 
# Number Guessing game!!!

"""import random
print("let's play the number guessing game")
print("The secret number is between 1 and 100") 
secretnum = random.randint(1, 100)
guesses = 0
while guesses <= 10:
    guess = int(input("Enter your guess: "))
    guesses += 1   
    if guess < secretnum:
        print("Too low! Try again.")
    elif guess > secretnum:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number in", guesses, "guesses.")
else:
    print("Game Over! Better luck next time")
    """


# LOOPS COMPLETED!!!!!!!