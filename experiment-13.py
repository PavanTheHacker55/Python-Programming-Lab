# Write a program to: Create dictionary, add element to dictionary, delete element
# from the dictionary.

# 1. Creating a Empty Dictionary
dictionary = {} # [or] dictionary = dict()
print(dictionary)

# 2. Adding Elements to the Dictionary
dictionary[1] = "Pavan"
dictionary[2] = "Teja"
dictionary[3] = "Maahi"
print(dictionary)

# 3. Deleting Elements from Dict
del dictionary[2]
print(dictionary)

dictionary.pop(3) # to remove specified key element
print(dictionary)

dictionary.clear() # to remove all elements
print(dictionary)