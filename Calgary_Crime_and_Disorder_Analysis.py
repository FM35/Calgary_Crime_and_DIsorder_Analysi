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
Crime_and_Disorder = Crime_and_Disorder.drop(['Crime Count' , 'ID', 'Sector', 'Community Center Point'], axis = 1)
Crime_and_Disorder['Date'] = Crime_and_Disorder['Date'].str[-2:]

#Splitting the table into crime and disorder
Crime = Crime_and_Disorder[Crime_and_Disorder['Group Category'] == 'Crime']
Disorder = Crime_and_Disorder[Crime_and_Disorder['Group Category'] == 'Disorder']

Crime_and_Disorder_by_Community = Crime_and_Disorder['Community Name'].value_counts()
Crime_by_Community = Crime['Community Name'].value_counts()
Crime_by_Year = Crime['Year'].value_counts()
Crime_by_Month = Crime['Month'].value_counts()
Disorder_by_Community = Disorder['Community Name'].value_counts()
Disorder_by_Year = Disorder['Year'].value_counts()
Disorder_by_Month = Disorder['Month'].value_counts()

#print(Crime_and_Disorder_by_Community[:20],Crime_by_Community[:20],Crime_by_Year,Crime_by_Month,Disorder_by_Community[:20],Disorder_by_Year,Disorder_by_Month)

def func1(dataframe,grouping_variable, num):

    common_for_each_grouping_variable = dataframe.groupby(grouping_variable).Category.value_counts()
    common_for_each_grouping_variable_index = common_for_each_grouping_variable.index
    index1 = [x[0] for x in common_for_each_grouping_variable_index]
    index2 = [x[1] for x in common_for_each_grouping_variable_index]

    crime_totals_for_each_category_per_grouping_variable  = pd.DataFrame({grouping_variable: index1 , 'Type': index2, 'Count' : common_for_each_grouping_variable.values})
    Most_common_crime_per_grouping_variable = crime_totals_for_each_category_per_grouping_variable.sort_values('Count', ascending = False ).groupby(grouping_variable).head(num)

    return Most_common_crime_per_grouping_variable

func1(Disorder, 'Community Name', 1).to_csv(r'C:\Users\HEATPACK_OLLIE\Desktop\Computer Science\Data Science\Git Repositories\CPS_Project\Most_Common_Disorder_for_each_Calgary_Community(2012-2019).csv', index = False)
func1(Disorder, 'Year', 1).to_csv(r'C:\Users\HEATPACK_OLLIE\Desktop\Computer Science\Data Science\Git Repositories\CPS_Project\Most_Common_Disorder_for_each_Year.csv', index = False)
func1(Disorder, 'Month', 1).to_csv(r'C:\Users\HEATPACK_OLLIE\Desktop\Computer Science\Data Science\Git Repositories\CPS_Project\Most_Common_Disorder_for_each_Month(2012-2019).csv', index = False)
func1(Crime, 'Community Name', 1).to_csv(r'C:\Users\HEATPACK_OLLIE\Desktop\Computer Science\Data Science\Git Repositories\CPS_Project\Most_Common_Crime_for_each_Calgary_Community(2012-2019).csv', index = False)
func1(Crime, 'Year', 1).to_csv(r'C:\Users\HEATPACK_OLLIE\Desktop\Computer Science\Data Science\Git Repositories\CPS_Project\Most_Common_Crime_for_each_Year.csv', index = False)
func1(Crime, 'Month', 1).to_csv(r'C:\Users\HEATPACK_OLLIE\Desktop\Computer Science\Data Science\Git Repositories\CPS_Project\Most_Common_Crime_for_each_Month(2012-2019).csv', index = False)