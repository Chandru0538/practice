#print("Question:1")
#Count Characters in a String:
#Description: Write a program that counts the occurrences of each character in a given string.
#Example:
#Input: "hello"
#Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
'''
Entity= count the characters of a string
Technical analysis:
State: str,
Behaviour: string methods, loops
Requirements: To count the occurance of the string
Functional Analysis:
1.Take input from the user
2.The input must be in string format
3.Iterate the input using for loop
4.Then count the occurence of the character in the string
'''
# string= input("Enter the word:")
# str2={}
# for i in string:
#     co=0
#     for j in string:
#         if i == j:
#             co=co+1
#             str2[i]=co
# print(str2)

# print("Question :2")
'''
Find Maximum and Minimum:
Description: Write a program to find the maximum and minimum numbers in a given list.
Example:
Input: [4, 9, 2, 7, 5]
Output: Maximum: 9, Minimum: 2

Entity=To find max and minimum numbers in a given
State: int, float
Behaviour: max min loops decision making
Functional analysis
1.take the input from the user
2.iterate the by using for loop
3.check the ma xvalue is equal to the i 
4.print it
 '''
# n=input("Enter the numbers seperated by using (,):").split(",")
# max=n[0]
# min=n[1]
# for i in n:
#     if max<i:
#         max=i
# print("The maximum value is : ",max)
# for j in n:
#     if min>j:
#         min=j
# print("The minimum value is : ",min)

# for i in n:
#     if max(n)==i:
#         print("The maximum value is : ",i)
#     elif min(n)==i:
#         print("The minimum value is : ",i)
'''
#print("Question :3")
Calculate Average:
Description: Write a program that calculates the average of a given list of numbers.
Example:
Input: [2, 4, 6, 8]
Output: 5.0
Entity = To calculate average
State: int
Behaviour:sum, division, length
Functional Analysis:
1.Take input from the user
2.Verify its a valid list
3.Find the sum of list
4.Find the length of list
5.Then divide the sum of list using length of the list
'''
# n=input("Enter the numbers seperated with commas").split(",")
# sum=0
#c=0
# for i in n:
#     sum+=i
#     c+=1
# print(sum)
# avg=sum/c
# print(avg)

#print("Question :4")
'''
Check Palindrome:
Description: Write a program to check if a given string is a palindrome.
Example:
Input: "racecar"
Output: True
'''
#
# input=str(input("Enter the string: "))
# co=""
# for i in input:
#     co=i+co
# if input == co:
#     print("true")
# else:
#     print("false")

# if input[0::] == input[::-1]:
#     print("The given string",input," is a palindrome")
# else:
#     print("The given string ",input," is not a palindrome")

#print("Question :5")
'''
Description: Write a program that removes duplicates from a given list.
Example:
Input: [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2, 3, 4, 5]
'''
# number=input("Enter the numbers seperated with commas: ").split(",")
# num=[]
# for i in number:
#     if int(i) not in num:
#         num.append(i)
#         print(list(num))

#print("Question :6")
'''
Reverse List Order:
Description: Write a program that reverses the order of elements in a given list.
Example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
'''
# num=[1, 2, 3, 4, 5]
# n=[]
# num=number=input("Enter the numbers seperated with comma : ").split(",")
# for i in num:
#     n.append(i)
# print(n[::-1])

#print("Question :7")
'''
Description: Write a program to check if a given number is an Armstrong number.
Example:
Input: 153
Output: True
'''
# num=int(input("Enter number : "))
# sum=0
# n=num
# while(n>0):
#     rem=n%10
#     sum+=rem*rem*rem
#     n=n//10
# if sum==num:
#         print(num,"is a Amstrong Number")
# else:
#         print(num,"is not a Amstrong Number")
#print("Question :8")
'''Description: Write a program that removes specified characters from a given string.
Example:
Input: "Hello World", ['l', 'o']
Output: "He Wrld"
'''
# input1=input("Enter the string")
# input2 = input("Enter the word to remove:")
# input3=[]
# for i in input1:
#     for j in input2:
#         if i != j:
#             input3.append(i)
# new_str =""
# for k in input3:
#     new_str += k
# print("Output: ",new_str)

#print("Question :9")
'''
Description: Write a program to check if a given number is a perfect number.
Example:
Input: 28
Output: True
'''
# num=int(input("Enter the number: "))
# sum=0
# if num>0:
#     for i in range(1,num):
#         if num % i==0:
#             sum+=i
#     if sum == num:
#         print(num,"its a perfect number")
#     else:
#         print(num,"its not a perfect number")
# else:
#     print("valid number")

#print("Question :10")
'''
Description: Write a program that prints all the prime factors of a given number.
Example:
Input: 24
Output: 2, 3
'''
# num = int(input('num:'))
# output = ""
# for i in range(2,num):
#     if num%i==0:
#         no_factor = 0
#         for k in range(2,i):
#             if i%k==0:
#                 no_factor+=1
#         if no_factor==0:
#             output+= str(i)+", "
#     else:
#         no_factor=0
#         for i in range(2,num):
#             if num%i==0:
#                 no_factor += 1
#         if no_factor==0:
#             output ="This number has no factors other than 1 & the same number"
#
# print("output:",output)

#print("Question :11")
'''
Description: Write a program to calculate the greatest common divisor (GCD) of two given numbers.
Example:
Input: 24, 36
Output: 12
'''
# num_1=int(input("Enter the number: "))
# num_2=int(input("Enter the number"))
# min=min(num_1,num_2)
# max=max(num_1,num_2)
# for i in range(1,min+1):
#     if num_1 % i ==0 and num_2 % i ==0:
#         gcd=i
# print("GCD : ",gcd)

#print("Question :12")
'''
Description: Write a program that counts the number of words in a given sentence.
Example:
Input: "Hello, how are you?"
Output: 4
'''
# inp=input("Enter:").split(" ")
# n=len(inp)
# print(n)

#print("Question :13")
'''
Description: Write a program that finds common elements between two given lists.
Example:
Input: [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
Output: [4, 5]
'''
# l1=list(input("Enter the number: "))
# l2=list(input("Enter the number: "))
# co=''
# for i in l1:
#     for j in l2:
#         if i == j:
#             co=i+co
# print(list(co))

#print("Question :14")
'''
Description: Write a program to calculate the square root of a given number using the Newton-Raphson method.
Example:
Input: 16
Output: 4.0
'''
# n=int(input('num: '))
# x=n
# while(1):
#     root=0.5*(x+(n/x))
#     #print(x)
#     if (round(root,3)==round(x,3)):
#         break
#     x=root
# print(round(root,2))

#print("Question :15")
'''Swap Case:
Description: Write a program that swaps the case (upper to lower and vice versa) of each character in a given string.
Example:
Input: "Hello, World!"
Output: "hELLO, wORLD!"
'''
# string=input("Enter the string:")
# res=string.swapcase()
# print(res)
# res=''
# for i in string:
#     if i == i.upper():
#         res+=i.lower()
#     else:
#         res+=i.upper()
# print(res)

#print("Question :16")
'''
Description: Write a program that checks the strength of a password based on the following criteria:

Contains at least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Example:
Input: "Passw0rd"
Output: Strong password
'''
# passwd = input("Enter your password to validate : ")
# sp_chr = "!@#$%^&*()_-+=|?/<>.,`~"
# sp_c = 0
# num = 0
# if passwd:
#     if len(passwd) >= 8:
#         if passwd[0].isupper():
#             for i in passwd:
#                 if i.isdigit():
#                     num += 1
#                 for j in sp_chr:
#                     if i == j:
#                         sp_c += 1
#                         break
#             if sp_c >= 1 and num >= 1:
#                 print("Password is strength is good")
#             else:
#                 print("Password should contain at least one special character and one number")
#         else:
#             print("first letter should be capital")
#     else:
#         print("password must be 8 characters length")
# else:
#     print("Invalid input")

#print("Question :17")
'''
Description: Write a program that capitalizes the first letter of each word in a given sentence.
Example:  BGBGGB 
Input: "hello world"
Output: "Hello World"
'''
#input =input('Enter the word : ').split()
#stri=input1.capitalize()
#print(stri)
# new_sent = ""
# for word in input:
#      print((word[0]).upper() + word[1:])
#     new_sent += new_word + " "
# print(new_sent)

'''
#print("Question :18")
Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}'''
# input =input("Enter string: ").split()
# str2={}
# for i in input  :
#     co=0
#     for j in input :
#         if i == j:
#             co=co+1
#             str2[i]=co
# print(str2)

#print("Question :19")
'''
Anagram Checker:
Description: Write a program that checks if two given strings are anagrams of each other.
Example:
Input: "listen", "silent"
Output: True
'''
# inp1=list(input("Enter the string 1 :"))
# inp2=list(input("Enter the string 2 :"))
# st=""
# st1=""
# inp1.sort()
# inp2.sort()
# for i in inp1:
#     st += i
# for i in inp2:
#     st1 += i
# print(st == st1)

#print("Question :20")
# Description: Write a program that calculates the transpose of a given matrix.
# Example:
# Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#print("Question :21")
'''
Binary to Decimal Converter:
Description: Write a program that converts a binary number to its decimal equivalent.
Example:
Input: "1010"
Output: 10
'''
# binary=input("Enter a binary number: ")
# decimal=0
# for i in range(len(binary)):
#      decimal += int((binary[len(binary)-i-1]))*(2**i)
# print(decimal)
#print("Question :22")
'''
Caesar Cipher:
Description: Write a program that encrypts a given string using the Caesar cipher technique.
Example:
Input: "Hello", shift=3
Output: "Khoor"
'''
# State
# input_word = input("Enter the word: ")
# encrypted_word = ""
#
# Behaviour
# for char in input_word:
#     ascii_value = ord(char)
#     shifted_value = ascii_value + 3
#     encrypted_char = chr(shifted_value)
#     encrypted_word += encrypted_char
# print("Encrypted word:", encrypted_word)


