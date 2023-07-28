'''str.split(sep=' ')
str.replace(old_substring, new_substring)
str.lower()
str.upper()
str.contains('pattern', case=False)
str.extract(regular_expression)
str.count('sub_string')
str.find( )
str.isalnum()
str.islower()
str.isupper()
str.isnumeric()
str.isspace()
len( )
cat( )
separator.join(str)'''
'''1.split()'''
s="hii hello welcome!"
s1=s.split()#it splits the string using specified charatcters,default is space
print("1.split method :",s1)

'''2.replace():'''
s1=s.replace("hii","Hii")#it replaces the string, it takes two arguments which word want to replace and what we have to place there
print("2.replace method :",s1)

'''3.lower():'''
s1=s.lower()
print("3.lower method :",s1)#it converts the whole string in to lower case

'''4.upper():'''
s1=s.upper()
print("4.upper method :",s1)#it converts the whole string in to upper case

'''5.contains():''' #it checks the string contains substring
s="Hii Buddy"#it returns true if the string1 words are present in string2
s1="Hii"#else it returns false
print("5. __contains__():",s.__contains__(s1))

'''6.extract():'''

'''7.count('sub_string'):'''
print("7.count method:",s.count("i"))#it returns the count of the specified word

'''8.find():'''
#if the value is present it gives the index else it gives -1
#it is same as the index method but in index method the value is not present it shows error
st="hii welcome"
print("8.find method:",st.find("l"))

'''9.isalnum()'''
#this method returns true if the alphabet or numbers which are present in the string
s1="alpha"
s2="123456_"#it wont allows special characters
print("9.s1=alpha  ,isalnum:",s1.isalnum())
print("9.s2=123456_ (no special char) ,isalnum:",s2.isalnum())

'''10.islower():'''
#it checks all the given string is in lower case or not
s1="hello world"
s2="Hello World"
print("10.s1=hello world  ,islower():",s1.islower())
print("10.s2=Hello World  ,islower():",s2.islower())

'''11.isupper()'''
#it checks all the given string is in upper case or not
s1="hello world"
s2="HELLO WORLD"
print("11.s1=hello world  ,isupper():",s1.isupper())
print("11.s2=HELLO WORLD  ,isupper():",s2.isupper())

'''12.isnumeric()'''
#it checks weather the given string is numbers or not
s3="1234567"
print("12.s1=hello world ,isnumeric:",s1.isnumeric())
print("12.s3=1234567     ,isnumeric:",s1.isnumeric())

'''13.isspace()'''

'''14.len( )'''
'''15.cat( )'''
'''16.separator.join(str)'''