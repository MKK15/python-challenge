
# coding: utf-8

# In[86]:


import pandas as pd
import numpy as np
import csv
import os


# In[236]:


heroes_csv= pd.read_csv("heroes.csv") #Note: combined source csv's in Csv Fix.ipynd
heroes_csv.head()
#heroes_csv.columns


# In[53]:


# Player Count
player_count= len(heroes_csv['﻿"SN"'].unique())
player_df= pd.DataFrame({"Total Players": [player_count]})
player_df


# In[47]:


### Purchasing Analysis (Total) ###

# Number of Unique Items
unique_items= len(heroes_csv["Item ID"].unique())

# Average Purchase Price
purchase_price= heroes_csv["Price"].mean()

# Total Number of Purchases
total_purchases= heroes_csv["Price"].count()

# Total Revenue
total_revenue= heroes_csv["Price"].sum()

# Create Purchasing Analysis df
purchasing_analysis= pd.DataFrame({"Number of Unique Items":[unique_items],"Average Price":[purchase_price],"Number of Purchases":[total_purchases],"Total Revenue":[total_revenue]})
purchasing_analysis


# In[215]:


### Gender Demographics ###
gender_total= heroes_csv["Gender"].count()

female_count= heroes_csv["Gender"].value_counts()["Female"]
male_count= heroes_csv["Gender"].value_counts()["Male"]
other_count= heroes_csv["Gender"].value_counts()["Other / Non-Disclosed"]

f_percent= female_count/gender_total
m_percent= male_count/gender_total
o_percent= other_count/gender_total
    
gender_df= pd.DataFrame({"Gender":["Female","Male","Other"],"Percentage of Players": [f_percent, m_percent, o_percent],"Total Count": [female_count, male_count, other_count]})      
gender_table= gender_df.set_index("Gender")
gender_table



# In[214]:


### Purchasing Analysis (Gender) ###
# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals

female_df = heroes_csv.loc[heroes_csv["Gender"] == "Female",["Gender","Price"]]
f_count= female_df["Price"].count()
f_average= female_df["Price"].mean()
f_value= female_df["Price"].sum()

male_df = heroes_csv.loc[heroes_csv["Gender"] == "Male",["Gender","Price"]]
m_count= male_df["Price"].count()
m_average= male_df["Price"].mean()
m_value= male_df["Price"].sum()

other_df = heroes_csv.loc[heroes_csv["Gender"] == "Other / Non-Disclosed",["Gender","Price"]]
o_count= other_df["Price"].count()
o_average= other_df["Price"].mean()
o_value= other_df["Price"].sum()


gender_analysis= pd.DataFrame({"Gender":["Female","Male","Other"],"Purchase Count":[f_count, m_count, o_count],"Average Purchase Price":[f_average, m_average, o_average],"Total Value":[f_value, m_value, o_value]})
gender_df= gender_analysis.set_index("Gender")
gender_df


# In[223]:


### Age Demographics ###
# Bin Ranges
bins= [0,18,25,30,1000]

group_names= ["<18","18-25","25-30",">30"]

# Push out bin
heroes_csv["Age Ranges"]=pd.cut(heroes_csv["Age"], bins, labels=group_names)

age_1= heroes_csv.loc[heroes_csv["Age Ranges"]=="<18",["Age Ranges","Price"]]
means_1= age_1["Price"].mean()
count_1= age_1["Price"].count()
value_1= age_1["Price"].sum()

age_2= heroes_csv.loc[heroes_csv["Age Ranges"]=="18-25",["Age Ranges","Price"]]
means_2= age_2["Price"].mean()
count_2= age_2["Price"].count()
value_2= age_2["Price"].sum()

age_3= heroes_csv.loc[heroes_csv["Age Ranges"]=="25-30",["Age Ranges","Price"]]
means_3= age_3["Price"].mean()
count_3= age_3["Price"].count()
value_3= age_3["Price"].sum()

age_4= heroes_csv.loc[heroes_csv["Age Ranges"]==">30",["Age Ranges","Price"]]
means_4= age_4["Price"].mean()
count_4= age_4["Price"].count()
value_4= age_4["Price"].sum()

means= means_1,means_2,means_3,means_4
count=count_1,count_2,count_3,count_4
value=value_1,value_2,value_3,value_4

age_demographics= pd.DataFrame({"Age Ranges":["<18","18-25","25-30",">30"],"Average Purchase Price":[means_1,means_2,means_3,means_4],"Purchase Count":[count_1,count_2,count_3,count_4],"Total Purchase Value":[value_1,value_2,value_3,value_4]})
age_df= age_demographics.set_index("Age Ranges")
age_df


# In[246]:


### Top Spenders ###
player_list= heroes_csv['﻿"SN"'].unique()

purchase_count= []
average_price= []
purchase_value= []

for player in player_list:
    player_df = heroes_csv.loc[heroes_csv['﻿"SN"'] == player,["Price",'﻿"SN"']]
    
    count= player_df["Price"].count()
    average= player_df["Price"].mean()
    value= player_df["Price"].sum()

    purchase_count.append(count)
    average_price.append(average)
    purchase_value.append(value)
    
    
top_spenders= pd.DataFrame({"SN":player_list,"Purchase Count": purchase_count,"Average Purchase Price": average_price,"Total Purchase Value": purchase_value})      
top_spenders_df= top_spenders.set_index("SN")
top_df= top_spenders_df.sort_values(by= "Total Purchase Value", ascending= False)

top_df.head()


# In[257]:


### Most Popular Items ###
item_list= heroes_csv['Item ID'].unique()

item_name= [] 
purchase_count= [] 
item_price= [] 
purchase_value= []

for item in item_list: 
    item_df = heroes_csv.loc[heroes_csv['Item ID'] == item,:]
    
    count= item_df["Price"].count()
    price= item_df["Price"].unique()
    name= item_df["Item Name"].unique()
    value= item_df["Price"].sum()

    purchase_count.append(count)
    item_price.append(price)
    item_name.append(name)
    purchase_value.append(value)
    
most_popular= pd.DataFrame({"Item ID":item_list,"Item Name":item_name,"Purchase Count": purchase_count,"Item Price": item_price,"Total Purchase Value": purchase_value}) 
popular_df= most_popular.set_index("Item ID")
popular_sort= popular_df.sort_values(by= "Purchase Count", ascending= False) 
popular_sort.head()


# In[256]:


### Most Profitable Items ###
item_list= heroes_csv['Item ID'].unique()

item_name= [] 
purchase_count= [] 
item_price= [] 
purchase_value= []

for item in item_list: 
    item_df = heroes_csv.loc[heroes_csv['Item ID'] == item,:]
    
    count= len(item_df["Price"])
    price= item_df["Price"].unique()
    name= item_df["Item Name"].unique()
    value= item_df["Price"].sum()

    purchase_count.append(count)
    item_price.append(price)
    item_name.append(name)
    purchase_value.append(value)
    
profit_items= pd.DataFrame({"Item ID":item_list,"Item Name":item_name,"Purchase Count": purchase_count,"Item Price": item_price,"Total Purchase Value": purchase_value}) 
profit_df= profit_items.set_index("Item ID")
most_profitable= profit_df.sort_values(by="Total Purchase Value", ascending= False) 
most_profitable.head()

