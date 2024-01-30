# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:25 2024

@author: APUGNALIN
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas
"""

import pandas as pd

file = pd.read_csv("country_data.csv")

print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age1 = 30
age2 = 25
age3 = 29
age = [30, 25, 29, 26, 22]
print(age)

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]
fruit_sizes = {
    'fruits': fruits,
    'sizes': size_nm}
df = pd.DataFrame(fruit_sizes)
print(df['sizes'].mean())
print(df[df["sizes"] > 10])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]
df['prices'] = prices
df.drop(columns =["sizes"], inplace=True) # makes the df change permanent
