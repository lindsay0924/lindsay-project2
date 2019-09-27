# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:29:44 2019

@author: user
"""

import pandas as pd
from pandas import ExcelWriter
import numpy as np
raw_data=pd.read_excel('Module 2 Project_Project Performance_v1(2).xlsx')
df= pd.DataFrame(raw_data, columns=['Quality Score','Process Days','Project Cost'])
def prob(x,y,z):
    if x >500 & y<13 & z<234000:
        p=7
    elif x <= 500 &y<13 & z<234000:
        p=6
    elif x > 500 & y >=13 & z<234000:
        p=5
    elif x >500 & y <13 & z>=234000:
        p=4
    elif x <=500 & y >=13 & z<234000:
        p=3
    elif x<=500 & y<13 & z>=234000:
        p=2
    elif x >500 & y >=13 & z>=234000:
        p=1
    else: p=0
    return p
df['p']= prob(df['Quality Score'],df['Process Days'],df['Project Cost'])
df