#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import numpy as np
enron_data = pickle.load(open("C:/Users/rockm/OneDrive/Documentos/GitHub/ud120-projects/final_project/final_project_dataset_unix.pkl", "rb"))
import pandas as pd

p=[]
q=[]
i=0
for key in enron_data:
#    if enron_data[key]['poi']==True:
    p.append(enron_data[key]['total_payments'])

df=pd.Series(p)
df=pd.to_numeric(df,errors='coerce')
print('Number of POIs:',len(df))
print('Percentage:',100*(df.isnull().sum()/len(df)),'%')
print('NaN for total_payments:',df.isnull().sum())

for key in enron_data:
    q.append(enron_data[key]['email_address'])
df1 =pd.Series(q)
df1=df1.replace('NaN',np.nan)
print(len(df1)-df1.isnull().sum())

'''
print('CEO:',enron_data['SKILLING JEFFREY K']['total_payments'])
print('Chairman:',enron_data['LAY KENNETH L']['total_payments'])
print('CFO:',enron_data['FASTOW ANDREW S']['total_payments'])
'''
