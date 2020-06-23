#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df_names = ['confirmed_global', 'deaths_global', 'recovered_global'] 
df_list = [pd.DataFrame() for df in df_names]
df_dict = dict(zip(df_names, df_list))


# In[3]:


url_part = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_'

for key, value in df_dict.items():
    value = pd.read_csv(url_part+key+'.csv', parse_dates=[0])
    
    value.rename(columns={'Province/State': 'Province_State', 'Country/Region': 'Country_Region'}, inplace=True)
    
    dim_col = value.columns[0:4]
    date_col = value.columns[4:]
    value = value.melt(id_vars = dim_col, value_vars = date_col, var_name = 'Date', value_name = key)
    
    value['Date'] = pd.to_datetime(value['Date'])
    
    df_dict[key] = value
    print(value.head())
    print (key+" cases dataframe created\n----------------------------------------------------------")


# In[4]:


join_on_col = ['Province_State','Country_Region','Lat','Long','Date']
df_COVID = df_dict['confirmed_global'].merge(df_dict['deaths_global'], on=join_on_col, how='outer')                                .merge(df_dict['recovered_global'], on=join_on_col, how='outer')
df_COVID.rename(columns = {'confirmed_global':'Confirmed', 'deaths_global':'Deaths', 
                              'recovered_global':'Recovered'}, inplace = True)


# In[6]:


# to fill the NaN in 'Province_State' columns with Countries name in 'Country_Region'
df_COVID['Province_State'] = np.where(df_COVID['Province_State'] == 'nan', 
                                      df_COVID['Country_Region'], 
                                      df_COVID['Province_State'])

# to fill the NaN in last three columns
df_COVID.iloc[0:,-3:] = df_COVID.iloc[0:,-3:].fillna(0)


# In[7]:


print(df_COVID.head())


# In[8]:


df_COVID.to_csv('COVID-19.csv', index=False)


# In[9]:

import pygsheets
#authorization using credentials
gdrive = pygsheets.authorize(service_file='/Users/eklav/Documents/My Tableau Repository/Datasources/COVID-DataSource/covid-viz-data-update-secret.json')
print("-----------------Authorized--------------------")

# WORLD DATA
sheet = gdrive.open('COVID-19')
print("-----------------Sheet Opened------------------")

wks = sheet[0]
print("-----------------First Sheet Accessed----------")

wks.set_dataframe(df_COVID,(1,1))
print("-----------------Data Updated------------------")
print("Last Updated World Data As On: ", df_COVID.Date.max())