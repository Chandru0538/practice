
''' Requirement : Adding Numbers
    =================================
        1. Count   : Only 2 numbers or more
        2. Type    : Only Positive or only Negative or both Pos,Neg
        3. Datatype: Only Int. Int/Float
        4. Zero    : 0 is allowed or not

        Scenarios:      I. Based on count
                            1. 2 numbers  (Robot)  4 + 5 = __9___
                            2. 3/4/5 numbers
                        II. Based on type
                            1. Both positive
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number(pos/neg), 0
                        III. Based on datatype
                            1. Both int
                            2. Both float
                            3. int + float
                            4. float + int


'''
print("================I. ADDITION OF NUMBERS================")
print("----------------SCENARIOS-----------------")

# Different use cases/scenarios
#Addition
#State
a=10
b=12
#Behaviour
c=a+b
#Display result to end user
print("Addition:", c)
print('==================================')


#Behaviour
c=a-b
#Display result to end user
print('subtraction:',c)

#Behaviour
c=a*b
#Display result to end user
print('Multiplication:',c)

#Behaviour
c=a\b
#Display result to end user
print('Division:',c)

#
#Behaviour
c=a\\b
#Display result to end user
print('Floor division:',c)