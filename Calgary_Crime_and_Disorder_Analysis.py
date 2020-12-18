import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()

#Preprocessing Data. Removed the Crime Count and ID columns, Edited the info in Date to just have either 'AM' or 'PM'. Changed Resident Count to an integer
Crime_and_Disorder = pd.read_csv('CPS_Project\Community_Crime_and_Disorder_Statistics__to_be_archived_.csv')
Crime_and_Disorder['Resident Count'] = Crime_and_Disorder['Resident Count'].str.replace(',','').astype({'Resident Count' : np.int64})
Crime_and_Disorder = Crime_and_Disorder.drop(['Crime Count' , 'ID'], axis = 1)
Crime_and_Disorder['Date'] = Crime_and_Disorder['Date'].str[-2:]

#Printing descriptives for Categorical and Numerical Data
print(Crime_and_Disorder.describe(include = 'all'))