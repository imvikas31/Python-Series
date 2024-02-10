# <<<<<<--------------- Python Day 2 --------------------->>>
#Strings: all three ways given below are valid.
str1 = 'Vikas'
str2 = "Singh"
str3 = '''This is string 3'''
str4 = """This is string 3"""
print(str1)
print(str2)
print(str3)
print(str4)

# Escape Sequence Characters ---> (\n),(\t)
#  \n : used for giving some pattern or to change the current line.
#  \t : used for giving tab space.
str5 = "This is Vikas Singh\n\tStudent at Galgotias University"
print(str5)

# Basic Operations on String --->
# String Concatenation : adding two strings is concatenation , the operator used for concatenation is '+' operator

str6 = "Vikas"
str7 = "Singh"
strFinal = str6 + " " + str7
print(strFinal)   #concatenating str6 and str7 tp give strFinal

# Determining Length of a string --->
str8 = "here we are determining the length of the string"
strLength = len(str8)
print(strLength)   #returns the length of the 'str8' string = 48

# Indexing In Python --> whenever a string is created in python , an index is automatic created that is called an index. Indexing starts with 0 in python. We can access any character in a string using index.

# we can not manipulate the characters in string using their index only we can access them

str9 = "Vikas Singh"
ch1 = str9[0]
print(ch1)
ch2 = str9[1]
print(ch2)
ch3 = str9[2]
print(ch3)

# Slicing in Strings ---> accessing any part of a string is called slicing that string.
str10 = "Vikas Singh"
str11 = str10[0:5]   #ending index is included.Default starting index is Zero. so str10[0:5] is same as str10[ :5]
print(str11)

str12 = "Vikas Singh"
str13 = str12[1 : len(str12)] 
# str13 = str12[1: ]   #Default ending index is last index. so str12[1 : ] is same as str10[ 1 : len(str12)]
print(str13)

# Negative Indexing
str14 = "Vikas Singh"
print(str14[-len(str14) : -1])

# Strings Function:
# 1.str.endthwith() --->> #return true if str15 ends with 'sh' otherwise returns false
str15 = "Vikas"
print(str15.endswith("sh"))   
print(str15.endswith("s"))  

# 2. str.capitalize() : makes the first character of strings as capital letter. Only works for single time
str15 = "vikas"
print(str15.capitalize()) 
print(str15)  # returns original value

# str.replace() : replaces a character with another character
str16 = "Vikas Singh"
print(str16.replace("i" , "x"))

# str.find() : returns the Ist index of the first occurence , if character does not occurs in the given string then  it returns -1.
str17 = "Vikas Singh"
print(str17.find("i"))  #returns 1 as i has first occurence at index 1

str18 = "Vikas Singh"
print(str18.find("L"))  # returns -1 as L does not occurs in the given string.

# str.count() : reutns the count of all the occurences of the given character or part of string.
str19 = "Vikassingh"
print(str19.count("i"))
print(str19.count("s"))
print(str19.count("h"))


# Lets Practice : 
# Ques : 1: WAP to take user's name as inout also print its length?

# name = input("Enter Your Name : ")
# print("Your Name Is : "+name)
# print("Length Of Your Name Is : ", len(name))

# Ques : 2: WAP to find the occurence of '$' in a string
str20 = "2000$"
str21 = "20$$$$$"
print(str20.find("$"))  #returns the first occurence
print(str21.count("$"))  #returns the total occurences


# Conditional Statements:

age = 18
if(age < 18):
    print("Not eligible to vote !!")
elif(age  == 18):
    print("Can vote next year !!")
elif(age > 18):
    print("Eligible to vote this year !!")

    