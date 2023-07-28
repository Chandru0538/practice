''' 1.Length of string'''
# string="Hii Buddy Welcome To Python"
# c=0
# for i in string:
#     c+=1
# print("Length of string is",c)

''' 2.Count characters in string '''
# co={}
# char=input("Enter character : ")
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# print(co)

''' 3.String slicing '''
# str=input("Enter the string:")
# print(str[2::])

''' 4.Replace first occurance character '''
# str1 = input("Enter the string::")
# str2 = input("Enter the charcter to replace::")
# str3 =str2+str1[1::]
# print(str3)

''' 5.Swapping chars in string '''
# string1=input("enter string : ")
# string=list(string1)
# st=""
# string[0],string[-1] = string[-1], string[0]
# for i in string:
#     st+=i
# print(st)

''' 6.Append chars to string at end '''
# inp=(input("Enterstring: "))
# app=input("char to append : ")
# res=inp+" "+app
# print(res)

''' 7.Substring replacement '''
# st=input("Enter string:")
# rep=input("Enter string to replace : ")
# rep1=input("Enter replacement : ")
# st=st.replace(rep, rep1)
# print(st)

# st=input("Enter string:")
# le=0
# for i in st:
#     le+=1
# for i in range(le):
#     string1 = st[le-1]+st[:le-1]
# print(string1)

''' 8.Length of longest string in python '''
# string=input("Enter the string: ").split(" ")
# c=0
# long=max(string,key=len)
# for i in long:
#     c+=1
# len=c
# print("longest string is:", long)
# print("Length of the string:", len)
####
# max_len = 0
# for i in range(5):
#     st = input('  Enter str: ')
#     len=0
#     for i in st:
#         len+=1
#     if len > max_len:
#         max_len = len
# print("Length of the longest string is",max_len)

''' 9.nth index character from string '''
# string =input("Enter the string: ")#.split()
# print(string[-1])

''' 10.First last chars swapping '''
# string=input("Enter the string: ")
# l = 0
# for i in string:
#     l += 1
# if l<2:
#     print("Enter a string with atleast 2 characters")
# else:
#     n_s = string[l-1]+string[1:(l-1)]+string[0]
#     print(n_s)

''' 11.Remove odd index values '''
# li=input("Enter the string: ")
# print(li[1:2])

'''12.Count words in a string'''
# s=input("Enter the string: ")
# c=input("Enter the word to count: ")
# co=0
# for i in s:
#     if i == c:
#         co+=1
# print(co)

''' 13.Upper lower case of a string '''
# s=input("Enter the string :")
# a=s.swapcase()
# print(a)

'''14. Sort unique words alphanumerically
'''
# word1 = input('Enter the word : ').lower()
# word=set(word1)
# a_n = "abcdefghijklmnopqrstuvwxyz0123456789"
# str1=""
# for i in a_n:
#     for j in word:
#         if i==j:
#             str1+=j
# print(str1)
######
# s = input("Enter string:")
# s1=set(s)
# s2=list(s1)
# alp=""
# num=""
# for i in s2:
#     if i.isalpha():
#         alp+=i
#     if i.isdigit():
#         num+=i
# n=sorted(num)
# a=sorted(alp)
# print("sorted numbers",n)
# print("sorted alphabets",a)

''' 15.Create html from string '''
# tag = input('tag: ')
# content = input('content: ')
# html_code = "<"+tag+">" + content +"<"+tag+"/>"
# print(html_code)

''' 16.Insert string in middle of speical chars '''
# inp=input("Enter the string:")
# special_char="!@#$%^&*()"
# res=special_char[-2]+special_char[3]+inp+special_char[3]+special_char[-1]
# print(res)

''' 17. 4 Copies of last 2 chars '''
# inp=input("enter the strings:")
# res=inp[-2]+" "+inp[-1]
# print((res,)*4)

''' 18.Length of first 3 Words or last 3 words '''
# words=(input("Enter the string: "))
# s=words[:3]
# a=words[-4:-1]
# print(s,a)

''' 19.Last part of string '''
# string=input("Enter the string: ")
# c=0
# for i in string:
#     if i ==" ":
#         c+=1
# print(string[-1])

''' 20.reverses a string if it's length is a multiple of 4 '''
# string=input("Enter the string: ")
# c=0
# for i in string:
#    c+=1
# if c == 4:
#     co=string[::-1]
#     print(co)
# else:
#     print("greater than 4")

# # if len(string) == 4:
# #     strin="".join(reversed(string))
# #     print(strin)
# # else:
# #     print("the length of string is greater than 4")

''' 21.Convert a given string to all uppercase '''
# string=input("Enter the string: ")
# print(string.upper())

'''22. program to sort a string lexicographically'''
# str_list = []
# for i in range(5):
#     string = input('str: ')
#     str_list+=
#     str_list.append(string)
# str_list.sort()
# for i in str_list:
#     print(i)

''' 23.program to remove a newline in Python '''
# wd=input("Enter the string: ")
# re=input("Enter the line to remove: ").strip()
# new_word=wd.replace(re)
# print(wd)
# print(wd+re)

''' 24.program to check whether a string starts with specified characters '''
# string=input("Enter the string: ")
# if string.startswith("a"):
#     print("true")
# else:
#     print("false")

''' 26.display formatted text (width=50) as output '''
# import textwrap
# inpu=input("Please enter:")
# res=textwrap.fill(inpu,width=500)
# print(inpu)
# print(res)

''' 27.remove existing indentation from all of the lines in a given text'''
# inp1=input('Enter the string :')
# c=""
# for i in inp1:
#     if i != " " :
#         c+=i
# print(c)

''' 28.to add a prefix text to all of the lines in a string '''
# inp=input('Enter the string :')
# add=input("Enter text to add :")
# res=add+(" ")+inp
# print(res)

''' 29.to set the indentation of the first line '''
# inp=input('Enter the string :')
# ind=input("Enter indentation:")
# res=ind+inp
# print(res)

''' 30.to print the following floating numbers upto 2 decimal places '''
# a=float(input("Number 1 : "))
# b=float(input("Number 2 : "))
# d=a/b
# print("floating numbers upto 2 decimal places",round(d,2))

''' 31.print the following floating numbers upto 2 decimal places with a sign'''
# a=float(input("Number 1 : "))
# b=float(input("Number 2 : "))
# d=a/b
# print("floating numbers upto 2 decimal places",round(d,2))

''' 32.print the following floating numbers with no decimal places'''
# a=float(input("Number 1 : "))
# b=float(input("Number 2 : "))
# d=a/b
# print(int(d))

''' 33.print the following integers with zeros on the left of specified width'''
# num_to_print = [5, 23, 456, 7890, 12]
# sp_wid= 6
# for num in num_to_print:
#     for_num = "{:0>{width}d}".format(num, width=sp_wid)
#     print(for_num)

''' 34.print the following integers with '*' on the right of specified width'''
# n=input("enter the number: ").split()
# width = int(input("Enter the width:"))
# for i in n:
#     res = i.ljust(width, '*')
#     print(res)

''' 35.to display a number with a comma separator'''
# num=input('Enter the number')
# c=","
# for i in num:
#     c+= i
# print(c)

''' 36.to format a number with a percentage'''
"ch"
# num= float(input('Number:'))
# res1=num*100
# res=round(res1,2)
# print(res,"%")

''' 37.to display a number in left, right and center aligned of width 10'''

# s=input("Enter the number:")
# res=s.ljust(10)
# res1=s.rjust(10)
# res2=s.center(10)
# print(res,"%")
# print(res1,"%")
# print(res2,"%")

# num = input("Enter the number: ")
# leng = 0
# dig = "0123456789"
# for i in num:
#     leng += 1
# for i in num:
#     if i in dig:
#         res = True
#     else:
#         res = False
#         break
# if res==True:
#     left_align = num+" "*(10-leng)
#     right_align = " "*(10-leng)+num
#     center_align = " "*((10-leng)//2)+num+" "*((10-leng)//2)
#     print("Left_align:",left_align)
#     print("Right_align:",right_align)
#     print("Center_align:",center_align)
# else:
#     print("Enter a valid input")

''' 38.to count occurrences of a substring in a string'''
# st1=input("Enter the string:")#.split()
# c=0
# for i in st1:
#     if i == " ":
#         c+=1
# print(c)

''' 39.reverse a string'''
# string=input("Enter the string:")
# res=string[::-1]
# print(res)

''' 40.reverse words in a string'''
# string=input("Enter the string:")
# res=string[::-1]
# print(res)

''' 41.strip a set of characters from a string'''

"ERROR"
# st=input("Enter the string:")
# st2=input("Enter the char to strip:")
# res=st.strip(st2)
# print(res)

''' 42.count repeated characters in a string'''
# string=input("Enter the string: ")
# res={}
# for i in string:
#     count = 0
#     for j in string:
#         if i == j:
#             count+=1
#             res[i]=count
#     else:
#         res[i] = count
# for i,j in res.items():
#     if j >=2:
#         print("count of repeated ",i,"is",j,end="\n")

''' 44.print the index of the character in a string'''
# st=input("Enter the string:")
# for i in enumerate(st):
#     print(i)

''' 45.check if a string contains all letters of the alphabet'''
# alp=("aqwertyuiopsdfghjklzxcvbnm")
# cap=("QWERTYUIOPASDFGHJKLZXCVBNM")
# st=input("Enter the string:")
# co = 0
# for i in alp:
#     for j in cap:
#         if i in st or j in st:
#             co += 1
#             if len(st) == co:
#                 print("true")
#             break
#         else:
#            print("false")


''' 46.convert a string in a list'''
# st=input("Enter the string:")
# print(list(st))

''' 47.lowercase first n characters in a string'''
# st=input("Enter the string:")
# n=int(input("enter index:"))
# res=st[:n].lower()+st[n::]
# print(res)

''' 48.swap comma and dot in a string'''
# str1 = input("Enter the string::")
# str2 = ""
# for i in range(0, len(str1)):
#     if str1[i] == ",":
#         str2 += "."
#     elif str1[i] == ".":
#         str2 += ","
#     else:
#         str2 += str1[i]
# print(str2)

''' 49.count and display the vowels of a given text'''
# co={}
# vowels =("aeiou")
# char=input("Enter character : ")
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# for i, j in co.items():
#     if i in vowels:
#         print(i,"=",j)


''' 50.split a string on the last occurrence of the delimiter'''
# stri=input("Please enter a string:")
# spl=input("Please enter a delimiter:")
# st=stri.split(spl)
# a=st[-1]
# print(a)
                    # or
# str1 = input("Enter the String:")
# de = input("Enter the Delimiter:")
# l1 = []
# str2 = ""
# c=0
# for k in str1:
#     c+=1
# for i in range(0,c):
#     if str1[i] == de[0]:
#         l1.append(str2)
#         str2 = ""
#     else:
#         str2 += str1[i]
# l1.append(str2)
# print(l1[-1])

''' 51.find the first non-repeating character in given string'''
# s=[]
# co={}
# char=input("Enter character : ")
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# for a,k in co.items():
#     if k==1:
#         s+=a
# print(s[0])

''' 52.print all permutations with given repetition number of given string'''
''' 53.find the first repeated character in a given string'''
# s=[]
# co={}
# char=input("Enter character : ")
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# for a,k in co.items():
#     if k>=2:
#         s+=a
# print(s[0])

''' 54.find the first repeated character of a given string where the index of first occurrence is smallest '''
# s=[]
# co={}
# char=input("Enter character : ")
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# for a,k in co.items():
#     if k>=2:
#         s+=a
# print(s[0])

''' 55.find the first repeated word in a given string'''
# s=[]
# co={}
# char=input("Enter character : ").split()
#
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# for a,k in co.items():
#     if k>=2:
#         s.append(a)
#     print("first repeated string:",s[0])
# else:
#     print("no strings were repeated")
##########
# State
str1 = input("Enter the sentence::")
l1 = []
l2 = []
dict1 = {}
# Behaviour
word = ""
for i in str1:
    if i != " ":
        word += i
    else:
        l1 += [word]
        word = ""
l1 += [word]
print(l1)
for i in l1:
    m1 = 0
    for k in i:
        m1 +=1
        l2 += [m1]
for i in l1:
    count = 0
    for j in l1:
        if i == j:
            count += 1
    dict1[i] = count
for i, j in dict1.items():
    if j == 2:
        print("the first repeated word in a given string is: ", i)
        break
else:
    print("NO repeated word in a given string")

''' 56.find the second most repeated word in a given string'''
# s=[]
# co={}
# char=input("Enter character : ").split()
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# print(co)
# for a,k in co.items():
#     if k>1:
#         s.append(a)
# print(s)
# print(s[1])

''' 57.remove spaces from a given string'''
# str1=input("Enter the string,:")
# c=""
# for i in str1:
#     if i != " ":
#         c+=i
# print(c)

''' 58.move spaces to the front of a given string'''
# st=input("Enter the string,:")
# s=int(input("Enter the num to inert spaces:"))
# res=st.rjust(s)
# print(res)

''' 59.find the maximum occurring character in a given string'''
# string= input("Enter the word:")
# str2={}
# c=0
# for i in string:
#     co=0
#     for j in string:
#         if i == j:
#             co=co+1
#             str2[i]=co
# print(str2)
# max1=1
# c=""
# for a1,s in str2.items():
#     if s>max1:
#         max1=s
#         c =a1
# print(c)

''' 60.capitalize first and last letters of each word of a given string'''
# str1=input("Enter the string,:")
# st1=str1[0]
# st2=str1[-1]
# rep1=str1[0].upper()
# rep2=str1[-1].upper()
# str4=str1.replace(st1,rep1) and str1.replace(st2,rep2)
# print(str4)

''' 61.remove duplicate characters of a given string'''
# string=input('Enter the string:').split()
# c=""
# for i in string:
#     if i not in c:
#         c+=" " + i
# # print(c)

''' 62.compute sum of digits of a given string'''
# su=input("enter the numbers comma seperated : ").split(",")
# su1=list(su)
# sum=0
# for i in su1:
#     sum= int(i) + sum
# print(sum)

''' 63.remove leading zeros from an IP address'''
# ip=input("Enter ip address : ")
# c=""
# for i in ip:
#     if int(i) != 0:
#         c+=i
# print(c)

''' 64.Reverse a given string  Input : "Python"   Output : "nohtyP" '''
# st=input("Enter the string : ")
# print(st[-1])

''' 65.Reverse each word in given string Input '''
# st=input("Enter the string : ")
# print(st[-1])

''' 66.Reverse each word and reverse word again. Input '''
# st=input("Enter the string : ")
# print(st[-1])

''' 67.that accepts a string and calculate the number of digits and letters '''
# inp=input("Enter the string: ")
# c=0
# c1=0
# for i in inp:
#     if i.isdigit():
#         c+=1
# print("The number of digits: ", c)
# for j in inp:
#     if j.isalpha():
#         c1+=1
# print("The number of letters: ", c1)