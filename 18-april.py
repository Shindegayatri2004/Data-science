# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 08:10:18 2025

@author: Hp
"""

#pip install regex

import re

#1..(dot)-matches any character except newline
print(re.findall(r"a.c","abc aac acc adc a-c"))

"""
a-> matches a letter 'a'
.->match any one character(except newline)
c->matches the letter 'c'
so overalll, its looking for a three character strings 
first letter is 'a'
middle will be any charcater
last letter is a 'c'
abc=a+ any letter +c
"""
#################################################################

#2. ^(caret)-matches start of the string
print(re.findall(r"^hello","hello world\nhello python"))

"""
^-> this is caret ,and it means:
    match the following pattern only if it apperas at the very
    start of the string.
    hello->this is the actual text you're trying to match.
    so ^ hello means:
        match the world "hello" only if it is at the begining 
        input:"hello world\nhello python"
        "hello world"
        "hello python"
"""
        
#####################################################################

#3. $ (dollar)-matches end of the string
print(re.findall(r"python$","hello python"))

"""
python->this is the text you're trying to match
$-> this means:
    match this ** only if it appers at the end of the string
    so python$ means:
        match the world 'python' only if it is at the very 
        end of the string
        """
#try this
re.findall(r"python$","hello python devloper") # o/p:empty list

########################################################################

#4.*(astrick)-0 or more of the precending characters
print(re.findall(r"ab*c","ac abc abbc abbbc"))

"""
pattern:ab*c
this pattern uses the astrick *,which is one of the module
breakdown:
    a->match character a
    b*->match zero or more b characters
    c->match character c
    word       matches ab*c    why
    ac          yes             'b'appers 0 times
    abc         yes             'b' appers once
    abbc         yes             'b'appers twice
    abbbc        yes              'b'appers thrice
    """
####################################################################

#5.+(plus)->1 or more of the precending characters
print(re.findall(r"ab+c","ac abc abbc abbbc"))

"""
ab+c
this pattern is uses the plus + quantifiers
which is closely related to the * we discussed before.
breakdown:
    a->matches the character 'a'
    b+->matches one or more 'b' charcters
    c->matches character c
    so the full pattern matches:
        'a' followed by at least one 'b',followed by 'c'
        lets chech each word:
            "ac": no 'b' between 'a' and 'c'.'b+'requires at least one
             "abc": one 'b' matches the 'ab+c'
                      """
################################################################

#6. ?(question)->0 or 1 of the precending character
print(re.findall(r"ab?c","ac abc abbc abbbc"))

"""
pattern:ab?c
breakdown:
    a->matches the character 'a'
    b?->match 0 or one 'b'
    c->match the charcter 'c'
    so the pattern matches:
        'a' followed by at most one 'b',followed by the 'c'
        word       matches ab*c    why
        ac          yes             'b' appers zero times(allowed)
        abc         yes             'b' appers once (allowed)
        abbc         no             'b'appers twice(not allowed)
        abbbc        no              'b'appers thrice(not allowed)
        
        """
###############################################################
#7.{}(curly braces)-exact or range of the repetations
print(re.findall(r"ab{2}c","abc abbc abbbc abbbbc"))
print(re.findall(r"ab{4}c","abc abbc abbbc abbbbc"))
"""
pattern:ab{2}c
breakdown:
    a->matches the character 'a'
    b{2}->match exactly 2 'b' characters
    c->matches the character 'c'
    so this regex will only match:
        'a' followed by excatly 2 'b' ,followed by 'c'
        i.e., the string "abbc"
        """
##############################################################

#8.[](square brackets)-either b or c character set are allowed
print(re.findall(r"a[bc]d","abd acd aad aed"))

""" pattern:a[bc]d
breakdown:
    a->matches the charcter 'a'
    [bc]->match exactly one charcter,
    and it must be either 'b' or 'c'
    d->match the charcter 'd'
    so, this pattern matches:
        the string 'a' followed by either 'b' or 'c' """

##################################################################

# 9.[^](negated sets)-not in the set
print(re.findall(r"a[^bc]d","aad aed acd abd"))

"""
pattern:a[^bc]d
breakdown:
    a->matches the a character
    [^bc]->matches any one character except 'b' or 'c'
    the caret ^ inside square brackets negates the set.
    d->matches the character 'd'
    so this pattern matches:
        'a' followed by any character that is not b or c
        """
##################################################################g














