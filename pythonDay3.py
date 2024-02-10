#************************ List and Tupples ********************#
#All power is within you,you can do anything and everything - Swami Vivekanandan.

# List in Python : List in python is as same as Array in some other programming language.
# List is a BuiltIn Data Type.
# List is collection of element that can store data of any data type
#Lista are mutuable in python i.e it can be changed.
marks = ["karan","Vikas",67,"Abhinav",78,76,65,90]
print(marks)
print(marks[0])
print(marks[1])
print(len(marks)) # return  returns length of 'marks' list
print(type(marks))  # return  <class 'list'>

#Lista are mutuable in python i.e it can be changed.
# str = "vikas"
# print(str[0])
# str[0] = "A"  #Not posiible in case of string.

student = ["Vikas",21,9.05,"CSE"]
student[3] = "ECE"
print(student[3])
# print(student[4])  #return error -  "student" list index out of range

# List Slicing:print
print(student[ : 2])  # same asprint(student[0 : 2])
print(student[0: ])  # same asprint(student[0 : len(student)])
print(student[-4: -1]) 

# List Methods :
# 1.append:
age = [10,20,30,40,50]
age.append(15)  # mutation of the list.
print(age)

# 2. sort(): sorts in ascending order
age = [10,30,200,40,5]
age.sort() # sorts above list in ascending order
print(age)

# 3. sort(reverse = True): sorts in descending order
age = [10,30,200,40,5]
age.sort(reverse=True)  # sorts above list in descending order
print(age)

# 4. reverse(): reverse the lsit
age = [10,30,200,40,5]
age.reverse()  #reverse the above lsit
print(age)

# 5. insert(index, element):inserts element at the specified index
age = [10,30,200,40,5]
age.insert(0 , 1) #inserts 1 at 0th index.
print(age)

# 6. remove(element):removes the first occurence of the element.
age = [10,30,5,10,5]
age.remove(5) # removes the first occurence of the element.
print(age)

# 7. pop(element):removes element at any index.
age = [10,30,5,5,5]
age.pop(4) # removes element at any index.
print(age)

# Learn other List methods in pyhton Documentation.


# Tuples : Built in DataTypes in Python.It lets us create immutable sequences pof values.

tup = (12,23,34,45,56,6,77,88,9)
print(tup[0])
print(tup[1])
print(tup[2])

# Inserting elements in tuples are not allowed as tuples are immutable.
# tup[0] = 10   # not allowed return error

tup1 = () # creates an empty tuple.
print(type(tup1))
tup2 = (1 ,) # for single valued tuple it required to write the comma after the element
print(tup2)
print(type(tup2))

# Tuple Slicing : Slicing on tuple exactly works same as on List and strings.

#Tuple Methods:
tuple = (2,1,3,1)
print(tuple)
print(tuple.index(1))  #returns the index of the fist occurence of the specified element.
print(tuple.count(1))  #returns the count of total occurence of the specified element.

# Lets Practice --->>
# Ques:1: WAP to ask the user to enter the names of their 3 favourite movies and store them in a list.

# favMovie1 = input("Enter your first fovourite movie : ")
# favMovie2 = input("Enter your second fovourite movie : ")
# favMovie3 = input("Enter your second fovourite movie : ")



# favMovie = [favMovie1,favMovie2,favMovie3]
# print("Your favourite movies are : "+favMovie[0]+" , "+favMovie[1]+" , "+favMovie[2])

# Ques:2: WAP to check that if a lsit contains a plaindrome of elements.(Hint : use .copy() method)
list1  = [1,2 ,3,2 ,1]
copyList1 = list1.copy()
copyList1.reverse()

# list1 = input("Enter the elements of first list : ")
# list2 = input("Enter the elements of second list : ")

if(copyList1 == list1):
    print("First list is palindromic list")
else:
    print("First list is not a palindromic list")

