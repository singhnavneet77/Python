import pandas as pd
import numpy as np

diabetes_dataset = pd.read_csv('/Users/si00v/OneDrive/Desktop/My Coding/Python/Diabetes.csv')
type(diabetes_dataset)
# print(diabetes_dataset.head()) #First five row
# print(diabetes_dataset.tail()) #Last five row


# Creating a Datafream with rodom value
random_df = pd.DataFrame(np.random.rand(20,10))
# print(random_df.head()) 


# Finding the number of rows and column
# print(diabetes_dataset.shape)
# print(diabetes_dataset.info())