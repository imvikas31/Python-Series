# Dictionary --->> These are built in data types used to store key:value pairs.
# These are unordered, mutable (changeable) and dont allow duplicates.


student = {
    "name" :"vikas singh",
    "age" : "27",
    "Enrollment" : "22SCSE2011220",
    "CGPA" : "9.05"
}


print(student)   # prints "student" dictionary
print(type(student))    # returns the type of the "Student" dictionary : <class 'disct'>
print(student["name"]) #returns value corresponding to "age"-key
print(student["age"]) #returns value corresponding to "name"-key
print(student["Enrollment"]) #returns value corresponding to "Enrollment"-key
print(student["CGPA"]) #returns value corresponding to "CGPA"-key
# print(student["marks"]) # throws an error as there is no key like - "marks"

# Let's see how Dictionary is mutable --->>

# Assigning new value correspondding to any exixting key:
student["name"] = "Saurabh"
print(student["name"])

# Adding new key:value pair to any exixting dictionary:
student["surname"] = "Singh"
print(student["name"] + " " +student["surname"])

# If we make any new key:value pair with where key is similar to some exixting key the key:value pair gets overwritten.

student["name"] = "23"
print(student)

# Null Dictionary --->>
null_dict = {
    "address" : "Noida",
    "district" : "GB Nagar"
}
print(null_dict)
print(null_dict["address"])
print(null_dict["district"])

# Let's see Nested Dictionary --->>
# Dictionary inside a dictionary 

dict = {
    "name" : "Rahul",
    "age" : "23",
    # nested dictionary - subjects
    "subjects" : {
        "Physics" : "50",
        "Chemistry" : "49",
        "Mathematics" : "50"
    }
}
print(dict)
print(dict["subjects"])  # returns "subjects" - dictionary that is inside the dict dictionary 

print(dict["subjects"]["Physics"])  # returns value corresponding the key - "Physics" of "subjects" - dictionary that is inside the dict dictionary 

print(dict["subjects"]["Chemistry"])  # returns value corresponding the key - "Physics" of "subjects" - dictionary that is inside the dict dictionary 

print(dict["subjects"]["Mathematics"])  # returns value corresponding the key - "Physics" of "subjects" - dictionary that is inside the dict dictionary 


# Dictionary Methods --->>
# Let's create a dictionary dictionary with Items  with items-name and their prices per kilogram as key:value pairs. Also include another dictionary inside "Items" - dictionary
Items = {
    "apple" : "95",
    "pine-apple" : "130",
    "grapes" : "160",
    "watermelon" : "15",
    "vegetable" :{
        "tomato" : "30",
        "onion" : "40",
        "chili" : "130",
    }
}
# 1. dictionary_name.keys() --->> returns all the keys of the given dictionary.
print(Items.keys())
        # returns a list (dictionary type) of all the keys of the "Items" dicitonary but not the key of the nested dictionary.
        # Output --->> dict_keys(['apple', 'pine-apple', 'grapes', 'watermelon', 'vegetable'])

# we can convert the dictionary to any other data type like to lsit type.

print(list(Items.keys()))
        # returns a list (list type) of all the keys of the "Items" dicitonary but not the key of the nested dictionary.
        # Output --->> (['apple', 'pine-apple', 'grapes', 'watermelon', 'vegetable'])

# Total number of key in any dicitonary --->>
print(len(Items.keys())) 
        # returns total no of key in "Items - dictionary" 
        # Output --->> 5
#Another way --->>
print(len(list(Items.keys()))) 
        # returns total no of key in "Items - dictionary" 
        # Output --->> 5


# 2. dictionary_name.values() --->> returns all the values of the given dictionary and key:value pairs of the nested dictionary.
print(Items.values())
        # returns a list (dictionary type) of all the values of the "Items" dicitonary and the key:value pairs of the nested dictionary.
        # Output --->> dict_values(['95', '130', '160', '15', {'tomato': '30', 'onion': '40', 'chili': '130'}])

# we can convert the dictionary to any other data type like to a list type.

print(list(Items.values()))
        # returns a list (list type) of all the values of the "Items" dicitonary and the key:value pairs of the nested dictionary.
        # Output --->> ['95', '130', '160', '15', {'tomato': '30', 'onion': '40', 'chili': '130'}]  

# Total number of key in any dicitonary --->>
print(len(Items.values())) 
        # returns total no of values in "Items - dictionary" 
        # Output --->> 5
#Another way --->>
print(len(list(Items.values()))) 
        # returns total no of values in "Items - dictionary" 
        # Output --->> 5


# 3. dictionary_name.items() --->> returns all the key:value pairs of the given dictionary as tuples
print(Items.items())
        # returns a list (dictionary type) of all the key:value pair of the "Items" dicitonary as a tuples.
        # Output --->> dict_items([('apple', '95'), ('pine-apple', '130'), ('grapes', '160'), ('watermelon', '15'), ('vegetable', {'tomato': '30', 'onion': '40', 'chili': '130'})])

# we can convert the dictionary to any other data type like to a list type.

print(list(Items.items()))
        # returns a list (list type) of all the key:value pair of the "Items" dicitonary as a tuples.
        # Output --->>[('apple', '95'), ('pine-apple', '130'), ('grapes', '160'), ('watermelon', '15'), ('vegetable', {'tomato': '30', 'onion': '40', 'chili': '130'})] 


# dictionary_name["key_name"] ---> if the key_name mentioned into the method is not present in the dictionary the it  the throws an error and flow of program stips/breaks.
# print(Items["apple1"])  # since "apple1" key is not present is the "Items" dictionary so it throws an error.

# 4. dictionary_name.get("key_name") ---> if the key_name mentioned into the method is not present in the dictionary the it does not the throws any error but give "None" as output and flow of program continues.

print(Items.get("apple1"))  # since "apple1" key is not present is the "Items" dictionary so instead of throwing an error it gives "None" as output becaused we used .get() method.

# 4. dictionary_name.update() --->> inserts the specified items to the dictionary. We can also pass new Dictionary to an exixting dictionary using this function.

print("BEFORE")
Items.update({"Lichi" : "200"})
print(Items)

print("AFTER")
newDict = {
    "rasion" : "1200"
}
Items.update(newDict)
print(Items)


# Sets in Python ---->> Collection of unordered elements where each element in the set must be unique and immutable.

# NOTE ---->> sets are mutable but its elements must not be mutable

set1 = {1,2,3,4,5}
print(set1)     # returns {1, 2, 3, 4, 5}
print(type(set1))       # returns <class 'set'>

set2 = {1,2,2,2,2}  # repeated element are only stored once Bydefault. so this set resolves to {1,2}
print(set2)     #returns {1, 2}
print(type(set2))       # returns <class 'set'>


# list and dictionay can not be stored in set as list and dictionary are mutable(changeable)

null_set = set()   #syntacx for empty set.
print(null_set)    # returns set()
print(type(null_set))       # returns <class 'set'>

# Length of Set --->> using len() method
print(len(set1))        # returns 5
print(len(set2))        # returns 2
print(len(null_set))    # returns 0


# Set Methods ---->> 
# 1. set.add() --->> adds an element to the set
set3 = set()
set3.add(1)
set3.add(2)
set3.add(3)
set3.add(4)
print(set3)     #returns {1,2,3,4}

# 2. set.remove() --->> removes an element to the set
# set3.remove(5)  # throws error - KeyError: 5
# if key to be romeved is not present in the set then it throws an error -- > "keyError : key"
set3.remove(1)
print(set3)     #returns {2,3,4}

# 3. set.clear() --->> used to remove all the elements of the set at once
# set3.clear()
print(len(set3))        # returns 0
print(set3)     # returns set() means set3 is empty

# 4. set.pop() --->> removes a random element from the set
set3.pop() # remove any random element from set3.
print(set3)

# 5.set.union(set*) --->> combines the set values of set and set* and returns them.
set4 = {1,2,3,4}
set5 = {2,5,6,7}
print(set4.union(set5))  # returns {1, 2, 3, 4, 5, 6, 7}

# 6.set.intersection(set*) --->> combines the common set values of set and set* and returns them.
print(set4.intersection(set5))  # return "{2}" as "{2}" is common in both the set.

