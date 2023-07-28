'''1.Sum of elements'''
# l=input("Enter a list of: ").split()
# sum=0
# for i in l:
#     sum+=int(i)
# print(sum)

'''2.Mulitply of elements'''
# l=input("Enter a list of: ").split()
# sum=1
# for i in l:
#     sum*=int(i)
# print(sum)

'''3.Largest number from list'''
# l=input("Enter a list : ").split()
# print(max(l))

'''4.Smallest number from list'''
# l=input("Enter a list : ")
# print(type(l))
# print(list(l))
#
# print(min(l))

'''5.Count no of strings whose length is 2'''
# st=input("Enter a string: ").split()
# c=[]
# for word in st:
#     if len(word) == 2:
#         c.append(len(word))
#         print(word)
# print(len(c))

'''6.Sort elements in increasing order'''
# l= input("Enter the number:").split()
# li = list(l)
# li.sort()
# print(li)

'''7.Remove duplicates'''
# li1 = input("Enter the number:").split()
# li=list(li1)
# l=[]
# for i in li:
#     if i not in l:
#         l.append(i)
# l.sort()
# print(l)

# l=[1,2,3,3,3,4,5,6,7,8,7]
# l1=[]
# res=[l1.append(i) for i in l if i not in l1]
# print(l1)

'''8.Check list is empty or not'''
# l = input("Enter the number:").split()
# li = []
# if li == l :
#     print("the list is empty")
# else:
#     print("the list is not empty")

'''9.Clone or copy'''
# l=input("Enter The list :").split()
# li=list(l)
# lis=li.copy()
# print(lis)

'''10.Words that are longer than any element'''
# s=input("Enter the string:").split()
#
# for word in s:
#     print(len(word))
# ma=max(len(word))
# if max(len(word)) == ma:

'''11.Find common element from 2 lists'''
# l1=input("Enter the num:").split()
# l2=input("Enter the num:").split()
# res=[i for i in l1 if i in l2]
# print(res)

'''12.Remove specified index from list and print'''
# l=input("Enter the list:").split()
# l1=list(l)
# l1.pop(1)
# print(l1)

'''13.Write 3D array'''

'''14.Remove even elements and print list'''
# l=input("Enter the list:").split()
# l1=list(l)
# l2=[]
# for i in l1:
#     if int(i) % 2 ==1 :
#         l2.append(i)
# print(l2)

'''15.Shuffle list and print'''
# l=input("Enter the list:").split()
# l1=set(l)
# print(list(l1))

'''16.First,Last elements whose square value is between 1 and 30'''
# l=input("Enter the list:").split()
# l1=list(l)
# l2=[]
# for i in l1:
#     for j in range(0,30+1):
#         if int(i)*int(i) == j:
#             l2.append(i)
# res=l2[0],l2[-1]
# print(res)

'''17.First,Last elements whose square value is between 1 and 30,except first 5'''
# l=input("Enter the list:").split()
# l1=list(l)
# l2=[]
# for i in range(5,len(l)):
#     for j in range(0,30+1):
#         if int(i)*int(i) == j:
#             l2.append(i)
# res=l2[0],l2[-1]
# print(res)

'''18.All permutations of list elements'''

'''19.Difference betweeen 2 lists'''
# l=input("Enter the list:").split()
# l1=list(l)
# li=input("Enter the list:").split()
# l2=list(li)
# l3=[]
# l4=[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# for j in l2:
#     if j not in l1:
#         l4.append(j)
# print(l3+l4)

'''20.To access index of list'''
# l=input("Enter the list:").split()
# l1=list(l)
# for i in enumerate(l1):
#     print(i)

'''21.List of characters into string'''
# l=input("Enter a list of characters:").split(",")
# print(l)
# print(type(l))
# l2="".join(l)
# print(type(l2))

'''22.Finding index of an item in specified list'''
# l = input("Enter a list:").split(",")
# l2=input("Enter an item:")
# print(l.index(l2))

'''23.Flatten a shallow'''
# l=[[1,2,3],[4,5,6],[7,8,9]]
# li=[j for i in l for j in i]
# print(li)

'''24.Append a list to second list'''
# li=input("List: ")
# l=list(li)
# lis=input("List: ")
# l2=list(lis)
# for i in l:
#     if i not in l2:
#         l2.append(i)
#         # l3=",".join(list(l2))
# print(l2)

'''25.Select an item randomly'''
# import random
# list1= input('space seperated items: ').split()
# rand_num = random.randint(0,len(list1)-1)
# rand_item = list1[rand_num]
# print("random index:",rand_num)
# print("item: ",rand_item)

'''26.Check circularly identical in two lists'''
'''27.Finding a second smallest number'''
# l = input("Enter a list:").split(",")
# l.sort()
# print(l[1])

'''28.Finding a second largest number'''
# l = input("Enter a list:").split(",")
# l.sort()
# print(l[-2])

'''29.Get unique values'''
# l = input("Enter a list:").split(",")
# l1=list(l)
# l2=[]
# res=[l2.append(i) for i in l if i not in l2]
# print(l2)

'''30.Frequency of elements'''
# co={}
# char=input("Enter character : ")
# for i in char:
#     count = 0
#     for j in char:
#         if i == j:
#             count+= 1
#             co[i]=count
# print(co)

'''31.Counting number elements within a specified ranges'''
# l = input("Enter a list:").split(",")
# n = int(input("Number: "))
# co = 0
# for i in range(0, n):
#     if l[i].isdigit():
#         co += 1
# print("Number elements within a specified ranges is",co)

'''32.Check a list contains sublist'''
# l = ["aaaa","ssss","dddd"]
# l3=[]
# for i in l:
#     for j in i:
#         l3.append(j)
# if len(l) == len(l3):
#     print("its not a substring")
# else:
#     print("its a substring")
# for i in l:
#     print(type(i))
#     if type(i) == list:
#         print("its a sublist")
#         break
# else:
#     print("its not a sublist")
# # print(type(l))

'''33.Generate all sublists'''

'''34.Printing elements in ascending order'''
# ele=input("Enter the strings: ").split()
# e=list(ele)
# e.sort()
# print(e)

'''35.Create a list by concatenating a given list which range goes from 1 to n'''
# l=input('Enter a list:').split()
# l1=list(l)
# l2=[]
# n=int(input('Number of items to concatenate:'))
# for i in range(0,n):
#     if l[i] in l:
#         l2.append(l[i])
# print(l2)

'''36.Variable unique identification number'''

'''37.Finding common items from two lists'''
# l=input("Enter the list1:").split()
# l1=list(l)
# li=input("Enter the list2:").split()
# l2=list(li)
# l3=[]
# for i in l1:
#     for j in l2:
#         if i == j:
#             l3.append(i)
# print(l3)

'''38.Change the position of every nth value with (n+1)th value'''
# l=input('Enter the list values:').split()
# l[0],l[-1]=l[-1],l[0]
# print(l)

'''39.Converting multiple integers into single integer'''

'''40.Split a list based on first character of word'''
# l=input('Enter the list string:').split()
# n=input('Enter the chatacter')
# for word in l:
#     if word.startswith(n):
#         print(word)

'''41.Create multiple list'''
# l1,l2,l3=["apple",["orange"],"banana"]
# print(l1)
# print(l2)
# print(l3)

'''42.Find missing and additional values'''
# l=input("Enter the list").split(",")
# l1=list(l)
# li=input("Enter the list2").split(",")
# l2=list(li)
# l3=[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print("Additional elements in list1 missing in list2:",l3)
# l4=[]
# for j in l2:
#     if j not in l1:
#         l4.append(j)
# print("Additional elements in list2 missing in list1:",l4)

'''43.Split a list into different variables'''
# l=input('List:').split(",")
# l1,l2,l3=l
# print(l1)
# print(l2)
# print(l3)

'''44.Generate group of five consecutive numbers in a list'''
# n=int(input("enter the num:"))
# l=[]
# for i in range(5):
#     c=n+i
#     l.append(c)
# print(l)

'''45.Convert a pair of values into a sorted unique array'''

'''46.Select odd items of a list'''
# l=input("Enter the list:").split()
# l1=list(l)
# l2=[]
# for i in l1:
#     if int(i) % 2 ==1 :
#         l2.append(i)
# print(l2)

'''47.Insert an element before each element of a list'''
# l=input('Enter a list:').split()
# l1=list(l)
# e=input('Enter element want to insert:')
# l2=[]
# for i in l1:
#     for j in(e,i):
#         l2.append(j)
#         l3=" ".join(l2)
# print(l3)

'''48.Print a nested lists (each list on a new line) using the print() function'''
# l1=list(input("Enter list:"))
# l2=list(input("Enter list:"))
# l3=list(input("Enter list:"))
# l=[l1,l2,l3,]
# print(l)
# for i in l:
#     print(i)

'''49.Convert list to list of dictionaries'''
# l1=list(input("Enter list:"))
# l2=list(input("Enter list:"))
# res=dict.fromkeys(l1,l2)
# print(res)

'''50.Sort a list of nested dictionaries'''

'''51.Split a list every Nth element'''
# l=input('Enter a list:')
# li=l[-1]
# l1=l.split(li)
# print(l1)

'''52.Compute the similarity between two lists'''
# l=input('Enter a list:').split()
# l1=list(l)
# li=input('Enter a list:').split()
# l2=list(li)
# l3=[]
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)

'''53.Create a list with infinite elements'''
# l=input("Enter the element: ").split()
# l1=list(l)
# print(l1)

'''54.Concatenate elements of a list'''
# l=input('Enter a list:').split()
# l1=list(l)
# e=input('Enter element want to insert:')
# l2=[]
# for i in l1:
#     for j in(e,i):
#         l2.append(j)
#         l3=" ".join(l2)
# print(l3)

'''55.Remove key values pairs from a list of dictionaries'''
# l=input("Enter list:").split()
# l1=list(l)
# li=input("Enter list:").split()
# l2=list(li)
# res=dict.fromkeys(l1,l2)
# del res[2]
# print(res)

'''56.Convert a string to a list'''
# l=input("Enter the element: ").split()
# l1=list(l)
# print(l1)

'''57.Check if all items of a list is equal to a given string'''
# list_1 = input('spc_sep_items: ').split()
# strin = input('str: ').split()
# string=list(strin)
# if list(string)==list_1:
#     print("All the items are same")
# else:
#     print("Items are different")

'''58.Replace the last element in a list with another list'''
# inp=input("enter the list:").split()
# inp1=list(inp)
# n_l=input("enter the list:").split()
# nl=list(n_l)
# inp1.pop()
# inp1.append(n_l)
# print(inp1)

'''59.Check if the n-th element exists in a given list'''
# inp=input("enter the list:").split()
# inp1=list(inp)
# print(inp1[-1])

'''60.Find a tuple, the smallest second index value from a list of tuples'''
# lt=input("enter the list:").split(",")
# l1=tuple(lt)
# li=input("enter the list:").split(",")
# l2=tuple(li)
# lis=input("enter the list:").split(",")
# l3=tuple(lis)
# l=[l1,l2,l3]
# l.sort()
# print(l)
# print(l[1])

'''61.Create a list of empty dictionaries'''
# n=int(input("Enter the range: "))
# l=[]
# for i in range(1,n):
#     l.append({})
# print(l)

'''62.Print a list of space-separated elements'''
# l=input("Enter the list: ")
# l1=str(l)
# l2="".join(l1)
# print(l2)

'''63.Insert a given string at the beginning of all items in a list'''
'''Insert an element before each element of a list'''
# l=input('Enter a list:').split()
# l1=list(l)
# e=input('Enter element want to insert:')
# l2=[]
# for i in l1:
#     for j in(e,i):
#         l2.append(j)
#         l3=" ".join(l2)
# print(l3)

'''64.Iterate over two lists simultaneously'''
# l=input("Enter the list1:").split()
# l1=list(l)
# li=input("Enter the list2:").split()
# l2=list(li)
# for i in (l1,l2):
#     print(i)

'''65.Access dictionary keys element by index'''
# d={"1":"apple","2":"orange","3":"black","4":"pineapple"}
# l=d.items()#l=d.keys()
# l1=list(l)
# print(l1[1])

'''66.Find the list in a list of lists whose sum of elements is the highest'''
# li=list(input("Enter list:"))
# lis=list(input("Enter list:"))
# lst=list(input("Enter list:"))
# list1=[li,lis,lst,]
# l2=[]
# sum=0
# sum1=0
# sum2=0
# for i in list1[0]:
#     sum+=i
# print(sum)
# for j in list1[1]:
#     sum1+=j
# print(sum1)
# for k in list1[2]:
#     sum2+=k
# print(sum2)
# s=[sum,sum1,sum2]
# a=max(s)
# print(a)
# for m in range(0,len(s)):
#     if a == s[m]:
#         print(list1[m])

'''67.Find all the values in a list are greater than a specified number'''
# l=input("Enter a list of:").split()
# l1=list(l)
# l2=[]
# n=int(input("Enter the value:"))
# for i in l1:
#     if int(i) > n :
#         l2.append(i)
# print("the values in a list are greater than a specified number", l2)

'''68.Extend a list without append'''
# l=input("Enter the list 1:").split()
# l1=list(l)
# li=input("Enter the list 1:").split()
# l2=list(li)
# l1.extend(l2)
# print(l1)

'''69.Remove duplicates from a list of lists'''
# l1=list(input("Enter list:"))
# l2=list(input("Enter list:"))
# l3=list(input("Enter list:"))
# list1=[l1,l2,l3,]
# l21 = []
# for i in list1:
#     a=set(i)
#     b=list(a)
#     b.sort()
#     l21.append(b)
#     l21.sort()
# print(l21)

#####    or    #######

# list1 = [[9, 9, 8, 8], [7, 5, 6, 1, 7], [5, 6, 1]]
# l4 = []
# # Behaviour
# for i in list1:
#     l5 = []
#     for j in range(0,len(i)):
#         if i[j] not in l5:
#             l5.append(i[j])
#     l4.append(l5)
# print("Duplicates Removed", l5)

'''70.Get the depth of a dictionary'''
'''71.Check if all dictionaries in a list are empty or not'''
k1=input("Enter keys:").split()
k=list(k1)
v1=input("Enter values:").split()
v=list(v1)
res=dict.zip(k,v)

'''72.Two digits m (row) and n (column) as input and generates a two-dimensional array.
   The element value in the i-th row and j-th column of the array should be i*j'''
'''73.A list contains group of strings.Convert each word to capital letter and print'''
# l=input("Enter the list: ").split()
# l1=list(l)
# print(l1)
# l2=[]
# for word in l1:
#     l2.append(word.upper())
# print(l2)

'''74.Reverse list of elements and print in upper case'''
# l=input("Enter the list: ").split()
# l1=list(l)
# l1.sort(reverse=True)
# print(l1)
# l2=[]
# for word in l1:
#     l2.append(word.upper())
# print(l2)

'''75.Write a Python program to convert month name to a number of days'''
import datetime

