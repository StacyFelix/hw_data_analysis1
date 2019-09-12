#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
pd.set_option('display.max_rows',10)


def count_top3(list_years, path_dir):
    list_df = []
    for year in list_years:
        full_path = os.path.join(path_dir,f"yob{year}.txt")
        df = pd.read_csv(full_path, names=['Name', 'Gender', 'Count'], encoding = 'ISO-8859-1')
        list_df.append(df)
    return pd.concat(list_df).groupby(['Name', 'Gender']).sum().sort_values('Count', ascending=0).head(3)


def count_dynamics(list_years, path_dir):
    list_df = []
    for year in list_years:
        full_path = os.path.join(path_dir,f"yob{year}.txt")
        df = pd.read_csv(full_path, names=['Name', 'Gender', 'Count'], encoding = 'ISO-8859-1')
        df['Year'] = year
        list_df.append(df)
    return pd.concat(list_df).groupby(['Gender', 'Year']).sum()


if __name__ == '__main__':
    
    path_names = 'E:/НЕТОЛОГИЯ_КУРСЫ/Профессия Питон/2ч Продвинутый PYTHON/++2.5Data_analysis1/hw_data_analysis1/names/'
    
    print(count_top3([1880], path_names))
    print(count_top3([1900, 1950, 2000], path_names))
    
    print(count_dynamics([1900, 1950, 2000], path_names))
    
          


# In[ ]:




