#!/usr/bin/env python
# coding: utf-8

# # Federal Spending and the Impact on Unemployment in Veterans
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# The problem I aim to address is the unemployment among veterans and how it relates to federal spending on veterans programs. This topic is crucial as large numbers of veterans struggle to find gainful eomployment after military seperation, which can lead to other issues involving impacts to mental, physical and emotional health. High unemployment rates among veterans lead financial hardship, mental health issues, and a loss of valuable skills in the workforce. Analyzing the effectiveness of current government programs in reducing veteran unemployment is essential to optimize resource allocation, improving support services, and effectively using taxpayer dollars.

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 1. What are the trends in veteran unemployment rates from 2014 up til now (excluding COVID years)?
# 2. How has the Department of Veterans Affairs' spending changed over the same period, particularly in programs aimed at employment support?
# 3. Is there a correlation between VA spending on employment programs and the unemployment rates among veterans?
# 5. Are any changes in veterans employment rates explauined by nationwide changes?

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# I want to examine the impacts of US spending on veterans employment programs and how it relates to veteran unemployment rates. By using government spending as the independent variable and veteran unemployment rates as the dependent variable, the regression analysis will help determine if increased spending correlates with a reduction in unemployment among veterans or if there is no significant relationship between the two variables. 
# 
# Once I have identified any possible trends in the data between the two, I will examine that against the unemployment percent of change for the entire US, to see if any trends identified by the spending analysis can be explained by a nationwide shift not related to veterans program spending.Using a correlation coefficient I can see if veterans unemployment decreased by 2% annually while national unemployment dropped by 1.5% during the same period.
# 
# Another visual would show veterans unemployment rates before and after significant increases in government spending on veterans employment programs. The chart could show veterans unemployment rates for two periods: before the spending increase and after the increase.
# 
# At the conclusion of this analysis I intend to show that there is a distinct relationship between government spending and veterans unemployment rates. I feel that the results will show that increses in spending result in decreases in eunemployment rates. 

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# In[17]:


# Import the BLS stats for veteran unemployment
import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BLS_API_KEY")

if not api_key:
    raise ValueError("For Me: The key is in your inbox, set the env variable again")

url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'
headers = {'Content-Type': 'application/json'}

payload = {
    "seriesid": ["LNS13049526"],
    "startyear": "2014",
    "endyear": "2024",
    "registrationkey": api_key
}

res = requests.post(url, json=payload, headers=headers)

if res.status_code == 200:
    data = res.json()
    records = []
    for series in data['Results']['series']:
        for item in series['data']:
            records.append({
                'year': item['year'],
                'period': item['period'],
                'value': item['value']
            })
    df = pd.DataFrame(records)
    df.to_csv('data/veteran_unemployment_bls.csv', index=False)
    print("download complete.")
    print(df.head())
else:
    print(f"Failed to retrieve data: {res.status_code}")


# In[14]:


# load the Federal spending for Veterans programs from 2014-2014 from csv
import pandas as pd

df2 = pd.read_csv('data/us_unemployment_rate_change_2014_2024.csv')
print(df2.head())


# In[15]:


# load total US unemployment rate of change from csv
df3 = pd.read_csv('data/veterans_program_spending_by_year.csv')
print(df3.head())


# I will merge the relevant information from the datasets using the year as a key. It is common to all the datasets and fits the goal of my analysis. The veterans unemployment rate data is broken down by month within the year, but I can create a calculated column for the annual stats when I clean the data to remove the COVID years. 

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[ ]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

