# print("Hello Ji,kaise ho saare")
# print("Welcome To Python tutorials")
# print("Hello Ji,kaise ho saare!!","Welcome To Python tutorials")   #prints the output in single line
# print(23)
# print(23+23)
# print(23-23)

#variables:
name = "Vikas Singh"  #string value
# name = 'Vikas Singh'  
# name = '''Vikas Singh'''  
# name = "Vikas Singh"  
age = 23  #integer value
price = 25.99  #float value

rollNo = None
eligible = False

age2 = age   #we can assign value of one variable (age = 23) to another variable (age2):
print("Name : ",name)
print("Age : ",age)
print("Age : ",age2)
eligible = False
print("RollNo : ",rollNo)
print("Eligible : ",eligible)

#Type() method in python --> Return Data Type:
print(type(name))    # Data Type --->> <class 'str'>
print(type(age2))    # Data Type --->> <class 'int'>
print(type(age))     # Data Type --->> <class 'int'>
print(type(price))   # Data Type --->> <class 'float'>
print(type(rollNo))   # Data Type --->> <class 'NoneType'>
print(type(eligible))   # Data Type --->> <class 'bool'>

#Keywords : in python keywords are reserved words that can not be used for another meaning through out the programme.

#Python is a case sensitive programming language --> Ex: apple and Apple is different.

#Operator ---:
# 1. Arithmetic operator :
#return sum of two number--->
a  = 10
b  = 10
sum = a+b
print("Sum of a and b is : ",sum)

#return difference of two number--->
a  = 10
b  = 10
diff = a-b
print("Difference of a and b is : ",diff)

#return product of th=wo number--->
a  = 10
b  = 10
prdct = a*b
print("Product of a and b is : ",prdct)

#return ratio of two number--->
a  = 10
b  = 10
divide = a/b
print("Ratio of a and b is : ",divide)

# 2.Modulus Operator(%) :
#return modulus of two number--->
a  = 1
b  = 10
mod = a%b
print("Ratio of a and b is : ",mod)

# 2.Power Operator (**) : 
#return x to the power of y --->
a  = 2
b  = 3
power = a**b
print("Value of a to the power b is : ",power)

# Relational Operator : 
x = 10
y   = 20
print(x == y)   #returns either true or false: output->false
print(x != y)   #returns either true or false: output:->True
print(x > y)   #returns either true or false:  output:->False
print(x < y)   #returns either true or false:  output:->True
print(x >= y)   #returns either true or false: output:->False
print(x <= y)   #returns either true or false: output:->True

# 3.Assignment Operator : 
num1 = 10
num1 +=10
# num = num1+10  #num = 10+10 = 20
print("Value of num is : ",num1)

num2 = 10
num2 -=10
# num2 = num2-10  #num = 10-10 = 0
print("Value of num is : ",num2)

num3 = 10
num3 *=10
# num3 = num3*10  #num = 10*10 = 100
print("Value of num is : ",num3)

num4 = 10
num4 /=10
# num4 = num4/10  #num = 10/10 = 1
print("Value of num is : ",num4)

num5 = 1
num5 %=10
# num5 = num5%10  #num = 10%10 = 0
print("Value of num is : ",num5)

# 4.Logical Operators:
c  = 20
d  = 40
print(not False)  #returns true
print(not True)   #returns false
print(not (c>d))   #returns true



val1 = True
val2 = True
val3 = False
val4 = False
# AND Operator --->
print(val1 and val2)    #returns true
print(val1 and val3)     #returns false

# OR Operator --->
print(val1 or val3)    #returns true
print(val2 or val3)     #returns true
print(val1 or val2)     #returns true
print(val3 or val4)     #returns false


# Type Conversion in Pyhton ---->>
# 1.Type conversion ---> automatic conversion done by the interpeter or compiler
p = 10
q = 10.4
sum1 = p+q   # p convereted to float value (10.0)
print(type(p))   #returns <class 'int'>
print(sum1)  #returns 10.0+10.4 = 20.4
    
# 2.Type Casting --->> manually conversion of data type bu the user
p = "10"
q = 10.4
sum1 = float(p)+q   # p convereted to float value (10.0)
print(type(float(p)))  #returns <class 'float'>
print(sum1)  #returns 10.0+10.4 = 20.4


# TaLing Inputs Fron the Users --->>
# Name = input("Enter Your name : ")
# print("Welcome !! ",Name)
# print(type(Name))

# By default the type of the data taken as input by the user is always of String type

#to conver the input in its actual data type we do like this --->>
age = int(input("Enter Your age : "))
print("Your age is : ",age)
print(type(age) , age)

age = float(input("Enter Your age : "))
print("Your age is : ",age)
print(type(age) , age)

age = bool(input("Enter Your age : "))
print("Your age is : ",age)
print(type(age) , age)


#Let's practice:
# Question:1: Write a program to take the input of two numbers and alse print their sum?
m = int(input("Enter your first number"))
n = int(input("Enter your second number"))

result = m+n
print("Sum of both the entered number is : " ,result)

# Question:2: Write a program to take the side of a square  as input and also print its area?

side = int(input("Enter the length of the side of square : "))
area = side*side
print("Are of the square is : ",area)

# Question:3: Write a program to take the input of two floating point numbers and also print their average?
u = float(input("Enter your first number"))
v = float(input("Enter your second number"))

avg = (u+v)/2
print("Average of entered two floating point numbers is : ",avg)