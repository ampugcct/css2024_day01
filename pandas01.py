# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:32:18 2024

@author: APUGNALIN
"""

import pandas

file = pandas.read_csv("insurance_data.csv", skiprows=6)

print(file)
print(file.info())
print(file.describe())
