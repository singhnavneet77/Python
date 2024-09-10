import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#<--------------------------------->
# Total bill vs Tip bill
tips = sns.load_dataset('tips')
# print(tips.head()) 


#<--------------------------------->
# Visulize the data
data = sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')
# print(data)
# print(sns.set_theme)

iris = sns.load_dataset('iris')
print(iris.head())

 