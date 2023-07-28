# capitalize() :: Returns a string where the first character is upper case.
print("------------- capitalize() -----------------")
s="hello world"
s1=s.capitalize()
print(s1)

# center() , ljust, rjust : Returns a space-padded string with the original string centered to a total of width columns.
print("------------- center() -----------------")
print("center() : returns center padded string with mentioned length")
str1 = 'hello world'
res=s.ljust(20)#ALIGNS THE STRING AT RIGHT
res1=s.rjust(20)#ALIGNS THE STRING AT LEFT
res2=s.center(20)#ALIGNS THE STRING AT CENTER
print(res)
print(res1)
print(res2)
print("-------------------------------------------------------------------------------------")

# count() : Counts how many times str occurs in string or in a substring of string.
str1 = 'hello world'
print("-------------  count() -----------------")
print(str1.count("l"))
print(str1.count("H"))

# encode() : Returns the encoded version of the string.
str1 = 'hello world'
print("-------------encode() -----------------")
str2 = str1.encode('UTF-8', 'strict')
print("encoded version:",str2)

# decode() : Decodes the string using the codec registered for encoding.
print("------------- decode() -----------------")
str1 = 'hello world'
print(type(str1))
str2 = str1.encode('UTF-8', 'strict')
print('decode() : Decodes the string using the codec registered for encoding..')
print("Decoded string        :", str2.decode('UTF-8', 'strict'))
print("-------------------------------------------------------------------------------------")

# startswith() : returns true if list starts with given char
print("------------- startswith() -----------------")
str1="hello world"
print(str1.startswith("h"))

# endswith() : returns true if end with mentioned suffix.
print("-------------endswith() -----------------")
str1 = 'hello world'
print(str1.endswith("d"))

# expandtabs() : expands tab to mentioned spaces, 8 being default.
str1 = 'h\te\tl\tl\to'
print("------------- expandtabs() -----------------")
print(str1.expandtabs(6))

# find() : returns the index (within mentioned limits) \n returns -1 if not found.
print("-------------find() -----------------")
str1="hello"
print(str1.find("e"))

# index() : returns the index (within mentioned limits) \n else raises exception'
print("------------- index() -----------------")
str1="Hii buddy"
print(str1.index("i",0,3))#character want to find & start index & end index

# isalnum() : returns true if string is alphanumeric
print("------------- isalnum() -----------------")
str1="asdfg"
str3 = "Aug231994"
print("alphabets:",str1.isalnum())
print("alnum:",str3.isalnum())

# isalpha() : returns true if all substrings are alphabets.
print("------------isalpha() -----------------")
print("alpha:",str1.isalpha())
print("alnum:",str3.isalpha())

# isdigit() :  returns True if all characters in the string are digits.
print("------------- isdigit() -----------------")
str2 = "23081994"
print("Alpha:",str1.isdigit())
print("Alnum:",str3.isdigit())
print("Num:",str2.isdigit())

# islower() : returns True if all characters are in lowercase
print("------------- islower() -----------------")
print("Alpha:",str1.islower())
print("Alnum:",str3.islower())
print("Num:",str2.islower())

# isnumeric() : returns true if all characters in the string are numeric
print("-------------isnumeric() -----------------")
print("Alpha:",str1.isnumeric())
print("Alnum:",str3.isnumeric())
print("Num:",str2.isnumeric())

# isspace() : returns true if all characters in the string are whitespaces
print("------------- isspace() -----------------")
empty_str1 = "  "
print("Alnum:",str2.isspace())
print("Num:",str2.isspace())
print("EMPTY SPACE:",empty_str1.isspace())

# istitle() : returns true if string is in titlecase
str1 ="hello buddy"
str2 = "Hello Buddy"
print("------------- istitle() -----------------")
print("small letters:",str1.istitle())
print("EACH WORD STARTS with caps:",str2.istitle())

# isupper() : returns True if all characters are in uppercase
print("------------- isupper() -----------------")
str1 ="hello buddy"
str2 = "HELLO BUDDY"
print("small letters:",str1.isupper())
print("uppercase:",str2.isupper())

# join() : joins strings with mentioned separator
print("-------------  join() -----------------")
st="^".join(str2)
print(st)

# len() : returns length
print("------------- len() -----------------")
str1 = 'hello world'
print(len(str1))

# lower() : converts string to all lowercase characters
print("-------------  lower() -----------------")
str1 = 'HELLO WORLD'
print(str1.lower())

# lstrip()\ rstrip() : returns a copy of the string with leading whitespace removed
print("-------------  lstrip() \ rstrip()-----------------")
l="        hello buddy"
l1="hello world************"
print("removed specified char right lstrip(""):",l.lstrip(" "))
print("removed specified char right rstrip("'*'"):",l1.rstrip("*"))

# strip() : Performs both lstrip() and rstrip() on string.strips where the desired characters were given
print("------------- strip() -----------------")
print("removed specified char using strip("'*'"):",l1.strip("*"))

# maketrans() : Returns a translation table to be used in translate function.
print("------------- maketrans() -----------------")

# translate() : Translates string according to translation table str(256 chars), removing those in the del string..
print("------------- translate() -----------------")


# max(str) : Returns the max alphabetical character from the string str.(Using ASCII Values)
print("------------- max(str) -----------------")
st="abcwertyuijn"
s1=max(st)
print(s1)

# min(str) : Returns the min alphabetical character from the string str.(Using ASCII Values)
print('------------- min(str) -----------------')
s2=min(st)
print(s2)

# replace(old, new [max]) : replace with given char
print('-------------replace() -----------------')
str1="Hello Buddy"
str2=str1.replace("Hello","Hii")
print("replaced:",str2)

# rfind() : returns the index (within mentioned limits) \n returns -1 if not found.
print("------------- rfind() -----------------")
str3=str1.find("e",1,-1)
print("the index of the given string:",str3)

# rindex() : Same as index(), but search backwards in string'
print("------------- rindex() -----------------")
str4=str1.rindex("d")
print("the rindex of the given string:",str4)

# split() : separates with spaces into lists
print("-------------  split() -----------------")
str1 = "separates with spaces into lists"
print(str1.split(" "))

# splitlines() : splits at line breaks & returns lists
print("------------- splitlines() -----------------")
str2 = "separates \nwith \nspaces \ninto \nlists"
print(str2.splitlines())

# swapcase() : Inverts case for all letters in string.
print("------------- swapcase() -----------------")
str1 = "HELLO world"
print(str1.swapcase())

# title() : returns title case (Capitalize each word of the string).
print("-------------  title() -----------------")
s="Capitalize each word of the string"
print(s.title())


# upper() : Converts lowercase letters in string to uppercase.
print("------------- upper() -----------------")
print(s.upper())

# zfill(width) : Returns original string leftpadded with zeros to a total of width characters;
# intended for numbers, zfill() retains any sign given (less one zero).
print("------------- zfill() -----------------")
print(str1.zfill(15))

# isdecimal() : returns true if all characters in the string are numeric
print("------------- isdecimal() -----------------")
s="1234"
s1="asdf"
s2="12.43"
print(s.isdecimal())
print(s1.isdecimal())
print(s2.isdecimal())

# casefold() : converts strings lower
print("------------- casefold() -----------------")
st="Hello bUDDY"
print(st.casefold())

# isidentifier() : checks if the string is valid identifier or not
#it doesn starts with a number or have any space it contains only alphanumeric and undrscore
print("------------- isidentifier() -----------------")
s1="mango_123"
st="Hello bUDDY"
print("st.isidentifier():",st.isidentifier())
print("s1.isidentifier():",s1.isidentifier())

# isascii() :method returns True if all the characters are ascii characters  (a-z).
print("------------- isascii() -----------------")
st="apple123"
print(st.isascii())