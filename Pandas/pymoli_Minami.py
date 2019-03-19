#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd
import numpy as np


# In[2]:


# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"
# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# In[3]:


#2 Player Count
Count_Total_Players = len(purchase_data.groupby('SN'))
Count_Total_Players_dic = {'Total Players' : [Count_Total_Players]}
pd.DataFrame(Count_Total_Players_dic)


# In[4]:


# 3 Purchasing Analysis (Total)
Number_of_Unique_Items = (len(purchase_data.groupby('Item Name')))
Ave_Price = ("$" + str(round(purchase_data['Price'].mean(),2)))
Number_of_Purchases = (len(purchase_data))
Total_Revenue = ("$" + str(purchase_data['Price'].sum()))


# In[5]:


# Create a dictionary and a dataset to show the Purchasing Analysis
Purchasing_Analysis = {'Number of Unique Items' : [Number_of_Unique_Items],'Average Price':[Ave_Price],'Number of Purchases':[Number_of_Purchases],'Total Revenue':[Total_Revenue]}
Purchasing_Analysis_df = pd.DataFrame(Purchasing_Analysis)
Purchasing_Analysis_df.head()


# In[57]:


#4 Gender Demographics
Gender_df = purchase_data.groupby(['Gender'])
Count_Data = Gender_df.agg({'SN':pd.Series.nunique,'Price':'sum'})
Gender_Analysis = pd.DataFrame(Count_Data)
#4-1 Count of Data
Gender_Analysis['Total Count'] = purchase_data['Gender'].value_counts()
#4-2 Percentage of Players
Gender_Analysis['Percentage of Players'] = Gender_Analysis['Total Count'] / Gender_Analysis['Total Count'].sum()
#4-3 Clean data and show only the necessary data
Gender_Analysis_clean = Gender_Analysis[['Total Count','Percentage of Players']]
Gender_Analysis_clean


# In[65]:


#5 Purchasing Analysis
#5-1 Rename and Clean
Purchasing_Analysis = Gender_Analysis_clean.rename(columns={'Total Count':'Purchase Count'})
del Purchasing_Analysis['Percentage of Players']
#5-2 Total Purchase Value
Purchasing_Analysis['Total Purchase Value'] = Gender_df['Price'].sum()
#5-3 Average Price
Purchasing_Analysis['Average Purchase Price'] = Purchasing_Analysis['Total Purchase Value'] / Purchasing_Analysis['Purchase Count']
#5-4 Avg Total Purchase per Person
Purchasing_Analysis


# In[8]:


#6 Age Demographics
bins = [0,9,14,19,24,29,34,39,40]
group_labels = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","+40"]
pd.cut(purchase_data['Age'],bins,labels=group_labels).head()


# In[9]:


#6 put the bins in the Dataframe
purchase_data['Age_Group'] = pd.cut(purchase_data['Age'],bins,labels=group_labels)
purchase_data.head()


# In[10]:


#6 Age Demographics
#6-1 Count
Group_Age = purchase_data.groupby(['Age_Group'])
Count_Age = purchase_data['Age_Group'].value_counts()
Age_Analysis = pd.DataFrame(Count_Age)
Age_Analysis_clean = Age_Analysis.rename(columns={'Age_Group':'Total Count'})
#6-2 Percentage of Players
Age_Analysis_clean['Percentage of Players'] = (Count_Age / Count_Age.sum())*100
Age_Analysis_clean


# In[11]:


#7 Purchasing Analysis (Age)
Age_Analysis_clean['Total Purchase Value'] = Group_Age['Price'].sum() 
Age_Analysis_clean['Average Purchase Price'] = Age_Analysis_clean['Total Purchase Value']/ Age_Analysis_clean['Total Count']
#Age_df['Avg Total Purchase per Person'] =

Age_Analysis_clean


# In[12]:


#8 Top Spenders
SN_Group = purchase_data.groupby(['SN'])
Count_SN = purchase_data['SN'].value_counts()
SN_Analysis = pd.DataFrame(Count_SN)
SN_Analysis['Total Purchase Value'] = SN_Group['Price'].sum()
SN_Analysis['Average Purchase Price'] = SN_Analysis['Total Purchase Value']/SN_Analysis['SN']
SN_Analysis_Sort = SN_Analysis.sort_values('Total Purchase Value',ascending=False)
SN_Analysis_Sort.head()


# In[28]:


#9 Most Popular Items
#9-1 Groupby
Group_Data = purchase_data.groupby(['Item ID','Item Name'])
Count_Data = Group_Data.agg({'Item Name':'count'})
Item_Analysis = pd.DataFrame(Count_Data)
#9-2 Purchase Count
Item_Analysis['Total Purchase']=Group_Data['Price'].sum()
#9-3 Item Price
Item_Analysis['Item Price']=Item_Analysis['Total Purchase']/Item_Analysis['Item Name']
Item_Analysis_Clean = Item_Analysis.rename(columns={'Item Name':'Count Total'})
#format change? Item_Analysis_Clean['Total Purchase'] = Item_Analysis_Clean['Total Purchase'].map('{:,.2f}'.format)
Item_Analysis_Clean


# In[29]:


#10 Most Profitable Items
Item_Analysis_Sort = Item_Analysis_Clean.sort_values('Total Purchase',ascending=False)
Item_Analysis_Sort.head(5)

