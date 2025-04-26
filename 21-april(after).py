# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 16:29:26 2025

@author: Hp
"""

import re

oyo_data="""
1. OYO12345 - Deluxe room in mumbai - 1500/night - 4.2
2. OYO67890 - premium suite in delhi -2500/night - 4.8
3. OYO54321 - Standard room in bengalaru - 1200/night - 3.9
4. OYO09876 - Economy room in chennai - 999/night - 4.0
"""
pattern=r"(OYO\d+)\s-\s([\w\s]+)\sin\s([\w\s]+)\s-\s(\d+)/night\s-\s(\d\.\d)"

"""
(OYO\d+)  captures the OYO room id
\s-\s separator-matches the literal hyphyns
([\w\s]+) captures the room type
\sin\s matches the word "in"
([\w\s]+) captures the location
(\d+) captures the price per night
""" 
matches=re.findall(pattern,oyo_data)

for oyo_id, room_type, city, price, rating in matches:
   print(f"id:{oyo_id} | type:{room_type} | city:{city} | price:{price} | rating:{rating}")                                                                

########################################################################
import re
room_details="""
OYO12345 - Deluxe room - amenties:free wifi,ac,breakfast,
OYO67890 - premium suite - amenties:free wifi, gym, pool,
OYO54321 - Standard room - amenties:ac,tv,laundary
"""
pattern=r"(OYO\d+)\s-\s([\w\s]+)\s-\samenties:\s(.+)"


matches=re.findall(pattern, room_details)
for oyo_id, room_type,amenties in matches:
    amenity_list = [a.strip() for a in amenties.split(",")]
    print(f"{oyo_id} | {room_type} | amenties:{amentity_list}")

