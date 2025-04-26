# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 15:08:55 2025

@author: Hp
"""

# -- coding: utf-8 --
"""
Created on Mon Apr 21 14:49:14 2025

@author: om
"""

# 10) | (OR)

import re

print(re.findall(r"cat|dog", "I have a cat and a dog."))
re.findall(r"cat|bat|rat", "The cat, bat, and rat are animals.")
re.findall(r"a(b|c)d", "abd acd aad")



# 11) () (parentheses) -grouping
import re
text = "abab ab ababab"
match = re.findall(r"(ab)+",text)
match

"""
In regex, parentheses () are used for:
Grouping
Capturing (to extract matches)
Use () to group part of your regex pattern.
This is useful when applying quantifiers like *, +, ?, or {} to multiple characters.

"""
import re

text = "ha haha hahaha"

matches = re.findall(r'(ha)+', text)
print(matches)

"""
(ha)+ → Match one or more repetitions of "ha"

Output: ['ha', 'ha', 'ha'] (captures only the last "ha" from each match)

"""
text = "Name: John, Age: 25"
match = re.search(r'Name: (\w+), Age: (\d+)', text)
print()
print(match.group(1))  # 'John'
print(match.group(2))  # '25'
"""
(\w+) → captures the name

(\d+) → captures the age
"""
re.findall(r'(?:ha)+', 'hahaha')  # Output: ['hahaha']

#non-capturing group

##################################################

#12) \d -digit
text = "123 abc 456"
match = re.findall(r"\d+",text)
match
#['123', '456']
#\d match digit from 0-9

####################################################

# 13) \D =non-digit
text = "123 abc 456 def ABC"
match = re.findall(r"\D+",text)
match
#[' abc ', ' def']

#############################################

# 14) \w
#capture letters (a-z A-Z), digits (0-9) , and underscore _
#i.e all alphanumeric and _
text = "user_123 and user-234"
match = re.findall(r"\w+",text)
match
######################################################

# 15)\W 
#except (a-z, A-Z, 0-9, _)
#it also inclue white space
text = "a_b 123 @!?"
match = re.findall(r"\W+",text)
match
#[' ', ' @!?']
############################################
#16) \s
"""
\s matches any whitespace character, including:
Space ' '
Tab \t
Newline \n
Carriage return \r
Form feed \f
Vertical tab \v
"""
text = "a b\tc\nd"
match = re.findall(r"\s+", text)
match
# [' ', '\t', '\n']

#\s single whitespace character
#\s+ one or more
#\s* zero or more

########################################################

# 17)\S
#match any character except whitespace
#opposite of \s

text = "a b\tc\nd\nabc"
match = re.findall(r'\S+',text)
match
#['a', 'b', 'c', 'd', 'abc']

####################################################

# 18)re.sub() - substitute using regex
text = "my number is 123-456-7890"
match = re.sub(r"\d{3}-\d{3}-\d{4}","--",text)
match

#\d{3} find exactly 3 digits
###############################################

#if we have to find pattern not substitute the 

text = "my number is 123-456-7890"
match = re.findall(r"\d{3}-\d{3}-\d{4}",text)
match
#['123-456-7890']

#############################################

# 19) re.split() - split by pattern

text = "apple,banana,mango;grapes"
match = re.split(r"[,;]",text)
match

#['apple', 'banana', 'mango', 'grapes']
###################################################

# 20) \b - word boundaries
text = "cat scatter caterpillar category catfish satcat"
matches = re.findall(r'\bcat\b', text)
print(matches)
#['cat']

match = re.findall(r"cat\b",text)
match
#['cat', 'cat']

match = re.findall(r"\bcat",text)
match
#['cat', 'cat', 'cat', 'cat']

"""
\b is a word boundary anchor. It doesn’t match a character, but a position between:

A word character ([a-zA-Z0-9_])
and

A non-word character ([^a-zA-Z0-9_]) or the start/end of the string

Pattern 	Meaning
\bword	    Word starting with word
word\b	    Word ending with word
\bword\b	Exact whole word match
"""
#############################################
###############################################

#use cases

# 1. extract order ids from log string

logs = """
[INFO] order ID: SWY123456 placed at 6:45PM
[INFO] order ID: SWY789123 placed at 7:45PM
"""
match = re.findall(r"SWY\d{6}",logs)
match

#['SWY123456', 'SWY789123']

# 2. validate email and phone nuber
customer_data = [{"email":"rahul.sharma@gmail.com","phone":"1234567890"},
                 {"email":"fake-email@.com","phone":"12345"}]

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
phone_pattern = r"^[6-9]\d{9}$"
for customer in customer_data:
    valid_email = re.match(email_pattern, customer["email"])
    valid_phone = re.match(phone_pattern, customer["phone"])
    print(f"validating{customer['email']}| email:{bool(valid_email)}| phone:{bool(valid_phone)}")
 
# 3.parse menu items and prices
menu="""
1. paneer butter masala - 250 
2. chicken biryani - 300
3. veg thali -180
"""

items=re.findall(r"(\d+\.\s[\w\s]+)-\s(\d+)",menu)
print(items)

"""
regex part 1.panner butter masala matches
\d+        matches one or more digits
\.         matches literal dot
\s         (spaces)space after one
[\w\s]+    matches words and spaces
-          literal dash
\s         space after dash
(\d+)       matches price
"""    
    
print("parsed menu items & prices:",items)   
    
# 4.identify discount codes in notification messages
notifications="""
Use code SWIGGY50 to get 50 % off.
Hurry! Apply code FIRST100 FOR 100 OFF.
""" 
discount_codes=re.findall(r"\b[A-Z]+\d*\b",notifications)
discount_codes
"""
part                  meaning
\b                   word boundary (ensures we're matching a whole world)
[A-Z]                letters from A TO Z
"""  

# 5.CLEAN CUSTOMER reviews (remove emojis and unwanted characters)

reviews=[
    "food was awesome #happy",
    "worst experiance @ever!!",
    ]

cleaned_reviews=[re.sub(r"[^\w\s.,!?]","",review) 
                 for review in reviews]
print("cleaned reviews:",cleaned_reviews)  

   
    
    
    
    
    
    
    
    
    
    
    
    
    