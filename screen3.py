from os import access
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import xlrd
import openpyxl
from pathlib import Path

df = pd.read_excel("atm.xlsx",engine='openpyxl')
print(df)

l2=[]
l1=[]
data1=df[["TIME"]]
access1=pd.Series(df["TIME"])
for i in access1:
    l1.append(i)
    

data=df[["AMOUNT"]]
access=pd.Series(df["AMOUNT"])
for i in access:
    l2.append(i)
print(l2)
print(l2)

plt.plot(l1, l2, label = "user") 
plt.legend() 
plt.show()