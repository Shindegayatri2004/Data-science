# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 08:13:49 2025

@author: Hp
"""
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

#creating pdf file
reader=PdfReader('C:/2-python_DS/python_tutorial.pdf')
#getting page no
print(len(reader.pages))
#getting specific page from pdf file
page=reader.pages[10]
#extrcat text from page
text=page.extract_text()
print(text)

#######################################################################

import re
chat2='Hi: i have a problem with my order number 412889912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

###################################################################

import re
chat1='Hi:hello, i am having an issue with my order # 412889912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat1)
matches

##################################################################

chat3='hi:my order 412889912 is having an issue,i was charged 300$ when online it says 280$'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat3)
matches

################################################################

def get_pattern_match(pattern,text):
    matches = re.findall(pattern,text)
    if matches:
        return matches[0]

"""
if there are matches ,matches will be list
matches[0] is the first item in the list
if thre is no matches it return empty
"""
get_pattern_match('order[^\d]*(\d*)', chat1)

#####################################################################
#retrive email id and phone
chat1 = 'hi: you ask lot of questions 1235678912,abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_)*@[a-z]*\.[a-zA-Z0-9]*',chat1)

chat2='hi:here it is :(123)-567-8912,abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_)*@[a-z]*\.[a-zA-Z0-9]*',chat2)

chat3='hi: yes,phone:1234567890 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_)*@[a-z]*\.[a-zA-Z0-9]*',chat3)

#########################################################################

#phone number
get_pattern_match('(\d{10})|(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\d{3}\)-\d{3}-\d{4})',chat3)

####################################################################

text="""

Born	Elon Reeve Musk
June 28, 1971 (age 53)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States (from 2002)
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Domestic partner	Grimes (2018–2021)
Children	at least 14, including Vivian Wilson[1]
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)
Occupation	
Co-Founder and CEO of xAI
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder of the Boring Company, X Corp., and
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
De facto leader of the Department of Government Efficiency
"""
get_pattern_match(r'age(\d+)',text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()

"""
bORN:Born matches the literal word "Born"
.* :matches any number of any charcters(except newlines)
\n: a newline
"""
###################################################################

import pandas as pd
import numpy as np

df=pd.read_csv("C:/1-python/income.csv",names=["name","Income"],skiprows=[0])

df.Income.describe()
df
df.describe()
df.Income.quantile(0)
df.Income.quantile(0.25,interpolation="higher")
df.Income.quantile(0.99)
df
df['Income'][3]=np.NaN
df
df.Income.mean()
df_new=df.fillna(df.Income.mean())
df_new
df_new=df.fillna(df.Income.median())
df_new






























