# This file to create sample data for Cost-constraint ...
import pandas as pd 
import numpy

df = pd.read_csv("D:\Downloads\car.data", )
df['buying'].replace(['vhigh','high', 'med','low'], [0, 1, 2, 3], inplace = True)
df['maint'].replace(['vhigh', 'high', 'med', 'low'], [0, 1, 2, 3], inplace = True)
df['doors'].replace(['5more', '4', '3', '2'], [0, 1, 2, 3], inplace = True)
df['persons'].replace(['2', '4', 'more'], [0, 1, 2], inplace = True)
df['lug_boot'].replace(['small', 'med', 'big'], [0, 1, 2], inplace = True)
df['safety'].replace(['low', 'med', 'high'], [0, 1, 2], inplace = True)
df['judge'].replace(['unacc', 'acc', 'good', 'vgood'], [0, 1, 2, 3], inplace = True)
df.sample(n=100).to_csv('C:/Users/taduc/OneDrive/Máy tính/mastering/templates/data.txt', sep = " ", index = False, header = False)



