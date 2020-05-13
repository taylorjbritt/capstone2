import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#


# creating pie charts for lived experiences

df_drop = pd.read_pickle('../data/pickles/df_drop.pkl')
df_drop_pie = df_drop

gov_list = ['Dominant Party', 'Foreign/Occupied', 'Indirect Military', 'Military',
       'Military-Personal', 'Monarchy', 'Oligarchy', 'Parliamentary Democracy',
       'Party-Military', 'Party-Personal', 'Party-Personal-Military Hybrid',
       'Personal Dictatorship', 'Presidential Democracy',
       'Provisional - Civilian', 'Provisional - Military', 'Warlordism']

for gov_type in gov_list:
    col_name = str(gov_type) + '-pop'
    df_drop_pie[col_name] = df_drop_pie[gov_type]*df_drop['population']

# group all rows by type of government
gov_pop_grouped = df_drop_pie.groupby('government').sum()


#this section needs to be updated so that the values are dynamic, time permitting
#divide rows by total world population over time
gov_pop_grouped.sum()/(3.213110*10**12)

#pull out values for different regime type totals divided by world population
experience_percentage_dict = {

'Dominant Party' :                   3.325908*10**(-1),   
'Foreign/Occupied'   :                  2.270447*10**(-3),   
'Indirect Military'    :             1.511745*10**(-3),  
'Military'           :               3.175100*10**(-2),  
'Military-Personal'   :              2.951316*10**(-2),   
'Monarchy'            :             1.803674*10**(-2),    
'Oligarchy'            :            7.299268*10**(-3),    
'Parliamentary Democracy'  :        3.000837*10**(-1),   
'Party-Military'            :       3.273761*10**(-3),    
'Party-Personal'              :      1.504153*10**(-2),    
'Party-Personal-Military Hybrid'  :   3.150453*10**(-2),    
'Personal Dictatorship'         :    6.170772*10**(-2),     
'Presidential Democracy'       :     1.613844*10**(-1),    
'Provisional - Civilian'       :     1.351994*10**(-3),     
'Provisional - Military'       :     1.999623*10**(-3),    
'Warlordism'                 :       6.796235*10**(-4)     
}

#consolidated into the three major categories
experience_percentage_dict2 = {
'Nondemocratic' : 1 - ( 0.001351994 + 0.001999623 + 0.0006796235 + 0.1613844 + 0.30008370000000006),
  'Democracy' : 0.1613844 + 0.30008370000000006,
    'Interim': (0.001351994 + 0.001999623 + 0.0006796235)
                              }

#nondemocratic and democracy decomposed
experience_percentage_dict3 = {'Dominant Party': 0.3325908,
 
'Indirect Military': 0.0015117449999999999,
'Military': 0.031751,
'Military-Personal': 0.02951316,
'Monarchy': 0.01803674,
'Oligarchy': 0.007299267999999999,
'Party-Military': 0.003273761,
'Party-Personal': 0.015041530000000001,
'Party-Personal-Military Hybrid': 0.03150453,
'Personal Dictatorship': 0.06170772000000001,
'Foreign/Occupied': 0.002270447,
'Presidential Democracy': 0.1613844,
'Parliamentary Democracy' : 0.30008370000000006,
'Interim': 0.0040312405,}

#plot simple pie chart

fig, ax = plt.subplots(figsize = (15, 15))
ax.pie(experience_percentage_dict3.values(), labels= experience_percentage_dict3.keys(), startangle = 70, rotatelabels=True,)
ax.set_title('How People Were Ruled, 1950-2006', fontsize = 18)
fig.savefig('../images/ruledpiesimple.png')

#plot complex pie chart
explode = np.ones(len(experience_percentage_dict3))*.1
fig, ax = plt.subplots(figsize = (15, 15))
ax.pie(experience_percentage_dict3.values(), explode = explode, labels= experience_percentage_dict3.keys(), startangle = 70, rotatelabels=True)
ax.set_title('How People Were Ruled, 1950-2006', fontsize = 18)
fig.savefig('../images/ruledpiecomplex.png')


