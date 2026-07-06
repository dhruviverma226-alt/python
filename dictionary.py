# dictionaries are comma seperated key value pairs.
# enclosed within {}. Dictionaries are mutable
# keys are unique and immutable.
# values can be mutable.
# syntax: {key1:value1, key2:value2, key3:value3}
# example-
# my_dict = {'name':'Dhruvi', 'age':20, 'city':'Pune'}
# print(my_dict)
# accessing elements in a dictionary/ fetching the values
# it doesn't fetch the value by index, it fetches the value by key.
# my_dict = {'name':'Dhruvi', 'age':20, 'city':'Pune'}
# print(my_dict['name'])

# updating the values in a dictionary
# my_dict = {'name':'Dhruvi', 'age':20, 'city':'Pune'}
# my_dict['age'] = 21
# print(my_dict)

# adding new key value pairs to a dictionary
# my_dict = {'name':'Dhruvi', 'age':20, 'city':'Pune'}
# my_dict['email'] = 'dhruvi@gmail.com'
# print(my_dict)
#  KEYS ARE IMMUTABLE, SO WE CAN'T UPDATE THEM

# get() method in dictionaries does same work as accessing elements in a dictionary
# get will give output as none if the key is not present in the dictionary
# membership operator- in: 
# in operator works only on keys and not the value. 
# it displays false if value is used instead of the keys.
# for example:
# print('name' in my_dict)
# update method: dict.update(dict2)
# dict.update(dict2) updates the dictionary with the key value pairs of dict2
# if the key is already present in the dictionary, it updates the value
# if the key is not present in the dictionary, it adds the key value pair to the dictionary
# pop()- function deletes the key value pair from the dictionary.
# popitem()- function deletes the last key value pair from the dictionary.
# clear()- function clears the dictionary.]

# working with keys and values in dictionaries
# keys cannot be lists, sets and dictionaries.
# keys can be string, int, float, booleans, tuples. => mutable data types
# keys can only be mutable data types
# values can be any datatypes.

# fetching the keys: it can be done with key()
# print(my_dict.keys())
# fetching the values: it can be done with values()
# print(my_dict.values())
# to print every key value pairs- items() is used
# example: print(my_dict.items())
# shallow and deep copy: 
# first import copy module
# import copy
# l1= [1, 2, [1,5,6], 30]
# l2 = copy.copy(l1)
