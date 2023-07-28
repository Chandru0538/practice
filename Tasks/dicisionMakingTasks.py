print("Question no:1")
'''
ENTITY:Even or Odd
STATE:
Variable: int , operators
Behaviour: NUMBERS, % ==
 '''
'''Ask students to write a Python program that takes an input from the user,
and determines if it is an even number or an odd number.'''
# n=int(input('Enter the number : '))
# if n%2 == 0:
#     print("The give number ", n, "is even number")
# else:
#     print("The given number ", n, "is odd number")

# print("Question no:2")
'''Have students create a program that prompts the user to enter their age.
Based on the input, the program should display different messages according to the following conditions:
If age is less than 18: "You are a minor."
If age is between 18 and 65: "You are an adult."
If age is 65 or older: "You are a senior citizen."'''
# age=int(input('Enter your age : '))
# if age < 18:
#     print("you are a minor")
# elif age >= 18 and age < 65 :
#     print("You are an adult")
# elif age >= 65 :
#     print("You are a senior citizen")

# print("Question no:3")
'''In this task, students should develop a program that calculates the discount amount
for a shopping cart based on the following conditions:
If the total price is greater than or equal to $100, apply a 10% discount.
If the total price is between $50 and $99.99, apply a 5% discount.
If the total price is less than $50, no discount is applied.'''

# total_price=float(input('Enter total_bill amount : '))
# if total_price >=100:
#     res=total_price * 10/100
#     print("your discount amount is:", res)
#     print( "Your bill amount afer 10% discount: ", total_price - res )
# elif total_price >= 50 and total_price <=99.99:
#     res1 = total_price * 5 / 100
#     print("your discount amount is:", res1)
#     print("Your bill amount afer 5% discount: ", total_price - res1)
# elif total_price <= 50:
#     print("no discount is applied")
#     print("Your bill amount:",total_price)

# print("Question no:4")
'''Ask students to create a program that simulates a simple quiz.
The program should present a series of multiple-choice questions to the user and keep track of their score.
At the end of the quiz, display the user's score as a percentage.'''
# score = 0
# questions_list = {"1) which operator is used for multiplication?\na) # \nb) - \nc) / \nd) *": "d",
#                   "2) what symbol is used for single line comment?\na) // \nb) ''' \nc) # \nd) ||": "c",
#                   "3) what is the answer for 89%10 ?\na) 9 \nb) 8 \nc) 8.9 \nd) 89 ": "a",
#                   "4) which method is used to add single item to a list?\na) add \nb) a&d \nc) append \nd) extend ": 'b',
#                   '5) which method is used to make string capitalize?\na) upper() \nb) lower() \nc) capitalize() \nd) bigger()': 'a'
#                   }
# for x in questions_list:
#     print(x)
#     answer = input("Enter your Answer : ")
#     if answer == questions_list[x]:
#         score = score + 1
#         print("correct answers : ",score)
# percentage = (score / no_of_questions) * 100
# print(percentage)

# print("Question no:5")
'''Have students create a program that generates a random number between 1 and 100.
The user should guess the number, and the program should provide feedback on whether the guess is too high or too low.
The program should continue until the user guesses the correct number.'''
# i=30
# while True:
#     n = float(input("Enter the number:"))
#     if n>i :
#         print("your guess is too high")
#     elif n<i:
#         print("your guess is too low")
#     else:
#         print("you are correct")
#         break

# print("Question no:6")
'''Calculate the sum of three given numbers, if the values are equal then return thrice of their sum'''
# num1=int(input("Enter number:"))
# num2=int(input("Enter number:"))
# num3=int(input("Enter number:"))
# if num1==num2 and num2==num3:
#     res=num1+num2+ num3
#     print(res*3)
# else:
#     print("Given numbers are not equal")

# print("Question no:7")
'''Python program to test whether a number is within 100 of 1000 or 2000.'''
# num=int(input("Enter the number: "))
# if num<=100:
#     print("The given number is within 100")
# elif num > 100 and num <= 1000:
#     print("The given number is within 1000")
# elif num > 1000 and num <= 2000:
#     print("The given number is within 2000")
# else:
#     print("the must be within 100,1000 and 2000")

# print("Question no:8")
'''Python program to count the number 4 in a given list'''
# list=[1,2,3,4,5,4,4,3,4,4,5,3]
# c=0
# for i in list:
#     if i == 4:
#         c+=1
# print(c)

# print("Question no:9")
'''Python program to test whether a passed letter is a vowel or not.'''
# word=str(input("Enter the word: "))
# vowels=['a','e','i','o','u']
# if word in vowels:
#     print("Its a vowel")
# else:
#     print("It's not a vowel")

# print("Question no:10")
'''Write a program that prompts the user to enter their age and determines if they are eligible to vote or not.
Example Input: 21'''
# age_vote = int(input("Enter your age: "))
# if age_vote >=18:
#     print("your eligible for voting" )
# else:
#     print("you were not eligible")

# print("Question no:11")
'''Create a program that checks if a given year is a leap year or not.'''
# year=int(input("Enter year: "))
# if year % 4==0 and year % 100 != 0 or year % 400 == 0:
#     print(year,"its a leap year")
# else:
#     print(year,"its not a leap")

# print("Question no:12")
'''Develop a program that accepts a student's score as input and returns their corresponding grade according to a grading scale.'''
# score=int(input("Enter the student score:"))
# if score >= 90 and score < = 100:
#     print("Your score is: ", score, "your grade is A+")
# elif score >= 80 and score =<89:
#     print("Your score is: ", score, "your grade is A")
# elif score => 70 and score <= 79:
#     print("Your score is: ", score, "your grade is B")
# elif score >= 60 and score < =69:
#     print("Your score is: ", score, "your grade is C")
# elif score = > 35 and socore <= 59:
#     print("Your score is: ", score, "your were pass")
# else:
#     if score< 35 :
#         print("You were fail")

# print("Question no:13")
'''Create a program that calculates a person's Body Mass Index (BMI) based on their height and weight.'''
# weight= float(input("Enter your weight in KG:"))
# height= float(input("Enter your height in Meters:"))
# BMI=weight/(height**2)
# print(BMI)

# print("Question no:14")
'''Develop a program that validates user input to ensure it meets specific criteria (e.g., length, format).'''
# user = input("Enter user id:")
# user_id = str(user)
# if len(user_id) >= 6 and user.isalnum() and user_id[0].isupper() and user_id[1:4].islower() and user_id[4:].isdigit():
#     print('Valid user id')
# else:
#     print('Invalid user id')

# print("Question no:15")
'''Write a program that converts a given temperature from Celsius to Fahrenheit or vice versa.
1 celcius =38.3 fahrenheit'''
# c= float(input("Temperature in celcius: "))
# f=(c*9/5)+32
# print(c,"degree celciusis equal to",f," fahrenheit")
# print("Question no:16")

'''Create a program that verifies a users login credentials (e.g., username and password).'''
# user_name=(input("Enter your username:"))
# password=(input("Enter your password: "))
# if len(user_name)>=8 and user_name[0].isupper() and"." in user_name and "@" in user_name:
#     print("valid username")
#     if len(password) >= 8 and password[0].isupper() and "@" in password:
#         print("valid password")
#     else:
#         print("invalid password")
# else:
#     print("invalid user_name")

# print("Question no:17")
'''Develop a program that performs different operations on a given string based on user input (e.g., length, reverse, uppercase).'''
# str_word= input("Enter the word:")
# #length
# print(len(str_word))
# #reverse
# print(str_word[::-1])
# #uppercase
# print(str_word.upper())

# print("Question no:18")
'''Create a program that calculates the final price of a product after applying a discount.'''
# total_price=float(input('Enter total_bill amount : '))
# if total_price >=100:
#     res=total_price * 20/100
#     print("your discount amount is:", res)
#     print( "Your bill amount afer 20% discount: ","The final_price is", total_price - res )
#
# print("Question no:19")
''' Email Validation
Description: Create a program that validates if a given email address is correctly formatted.
Example Input: "john.doe@example.com"
Example Output: "The email address is valid."'''
# email_address= input("Create email address: ")
# if len(email_address) >= 15 and email_address[0].isupper and "." in email_address and "@" in email_address :
#     print("it is valid")
# else:
#     print("it is not valid")

# print("Question no:20")
'''Develop a program that converts a given number from one number system to another (e.g., binary to decimal).'''
# binary=int(input("Enter a binary number : "))
# decimal=0
# for i in range(len(binary)):
#     decimal += int((binary[len(binary)-i-1]))*(2**i)
#     print(decimal)

# print("Question no:21")
'''Description: Write a program that allows two players to play the classic game of rock, paper, scissors and determines the winner.
Example Input: Player 1: "rock", Player 2: "scissors"
Example Output: "Player 1 wins!"'''
# while True:
#     player1 = input("PLAYER 1 INPUT : ")
#     player2 = input("PLAYER 2 INPUT : ")
#     if player1 == "rock" and  player2 == "scissor":
#         print("Player 1 is the winner")
#     elif player1 == "scissor" and player2 == "paper":
#         print("Player 1 is the winner")
#     elif player1 == "paper" and player2 == "rock":
#         print("Player 2 is the winner")
#     elif player1 == "rock" and player2 == "paper":
#         print("Player 1 is the winner")
#     elif player2 == "rock" and player1 == "scissor":
#         print("Player 2 is the winner")
#     elif player2 == "scissor" and  player1 == "paper":
#         print("Player 2 is the winner")
#     elif player1 == player2:
#         print("It's a tie!")
#     elif player1 or player2 == "stop":
#         print("Game over")
#         break
#     else:
#         print("your are the looser")

# print("Question no:22")
'''Currency Converter
Description: Create a program that converts an amount of money from one currency to another based on current exchange rates.
Example Input: Amount = $100, Currency = USD to EUR
Example Output: "The converted amount is €85.62."'''
# amount= float(input("Enter amount : "))
# exchange_amount= float(input("Enter exchange currency value : "))
# exc_amount = amount* exchange_amount
# if exchange_amount ==0 or amount==0 :
#     print("No need to exchange :", exc_amount)
# else:
#     print("Exchanged currency amount is:",exc_amount)

# print("Question no:23")

'''Password Strength Checker
Description: Develop a program that evaluates the strength of a user's password based on certain criteria (e.g., length, complexity).
Example Input: "Pa$$w0rd"
Example Output: "The password is strong."'''
# password= input("Enter password : ")
# if len(password) >= 8 and password[0].isupper() and password[1:4].islower() and "@" in password:
#     print("The password is strong")
# else:
#    print("The password is week")

#print("Question no:24")
'''Description: Write a program that handles different types of errors and displays appropriate error messages to the user.
Example Input: "5" (when expecting an integer)
Example Output: "Invalid input. Please enter a valid integer."'''
# value=input("Enter the value : ")
# if value.isdigit():
#     print("The given value is valid")
# else:
#     print("Invalid input.Please enter a valid integer")

# print("Question no:25")
'''
Task 25: Game Character Decision-Making
Description: Create a program that simulates decision-making for a game character based on different scenarios (e.g., fight or flee, choose a weapon).
Example Input: Scenario = "Encounter enemy"
Example Output: "You decide to fight the enemy.
'''

# scenario = input("Enter the scenario: ")
# if scenario == "Encounter enemy":
#     decision = input("Do you want to fight or flee? ")
#     if decision == "fight":
#         print("You decide to fight the enemy.")
#     elif decision == "flee":
#         print("You decide to flee from the enemy.")
#     else:
#         print("Invalid decision. Please choose between 'fight' or 'flee'.")
# else:
#     print("Unknown scenario. Please enter a valid scenario.")
