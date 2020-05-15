import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_corr(df,size=10):
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation = 'vertical');
    plt.yticks(range(len(corr.columns)), corr.columns)
    fig.savefig('../images/correlation_matrix')


if __name__ == '__main__':

    # checking out the REIGN dataset

    reign_df = pd.read_csv('../data/REIGN_2020_5.csv')

    #aggregate coup attempts/successes by year
    yearly_df = reign_df.groupby('year').sum()

    fig, ax = plt.subplots(figsize = (12, 8))
    ax.bar(yearly_df.index.values, yearly_df['pt_attempt'], color = 'blue')
    ax.bar(yearly_df.index.values, yearly_df['pt_suc'], color = 'red', width = .3)
    plt.xticks(rotation=45, fontsize = 14)
    plt.yticks(rotation=0, fontsize = 14)
    ax.set_ylabel('Coups', fontsize = 16)
    ax.set_xlabel("Year", fontsize = 16)
    ax.set_title('Coups and Coup Attempts by Year', fontsize = 18)
    fig.savefig('../images/coupsyearly.png')


    #aggregate coup attempts/successes by country
    attempted_coups_bycountry = reign_df.groupby('country').sum()['pt_attempt'].sort_values()
    suc_coups_bycountry = reign_df.groupby('country').sum()['pt_suc'].sort_values()

    num_ = 15
    # plot the number of coups for a given number of countries
    fig, ax = plt.subplots(figsize = (12, 8))
    ax.bar(attempted_coups_bycountry.index[-num_:], attempted_coups_bycountry[-num_:], color = 'blue', label = 'Coups Attempts')
    ax.bar(attempted_coups_bycountry.index[-num_:], suc_coups_bycountry[-num_:], color = 'red', width = .5, label = 'Successful Coups')
    # N = len(attempted_coups_govtype.index)
    plt.xticks(rotation=45, Fontsize = 14)
    plt.yticks(rotation=0, fontsize = 14)
    # ticklocations = np.arange(0,N)
    # ax.set_xticks(ticks = ticklocations -1)
    ax.set_title("Attempted Coups – Top 15 Countries", fontsize = 18)
    ax.legend(loc = 'best', fontsize = 14)
    ax.set_ylabel('Coups', fontsize = 14)
    ax.set_xlabel("Country", fontsize = 16)
    plt.tight_layout(pad=3, h_pad=None, w_pad=None, rect=None)

    fig.savefig('../images/coupsbycountry.png')

    #aggregate coup attempts by government type (I created a new dataframe for this for indexing consistency with the percentages)
    govt_grouped = reign_df.groupby('government').sum()[['pt_suc','pt_attempt']]
    govt_counts = reign_df.groupby('government').count()

    #calculate coup attempts divided by government types
    govt_grouped['pt_attempt_percent'] = govt_grouped['pt_attempt']/ govt_counts['leader']
    govt_grouped['pt_suc_percent'] = govt_grouped['pt_suc']/ govt_counts['leader']

    govt_grouped = govt_grouped.sort_values(['pt_attempt'])

    #plotting coups by government type
    #total

    fig, ax = plt.subplots(figsize = (12, 8))
    ax.bar(govt_grouped.index.values, govt_grouped['pt_attempt'], color = 'blue')
    ax.bar(govt_grouped.index.values, govt_grouped['pt_suc'], color = 'red', width = .5)
    # N = len(attempted_coups_govtype.index)
    plt.yticks(rotation=0, fontsize = 14)
    plt.xticks(rotation=90, fontsize = 14)
    # ticklocations = np.arange(0,N)
    # ax.set_xticks(ticks = ticklocations -1)
    ax.set_title('Coups and Coup Attempts by Government Type (total)', fontsize = 18)
    plt.tight_layout(pad=3, h_pad=None, w_pad=None, rect=None)
    fig.savefig('../images/coupsbygovttotal.png')

    #percentages
    fig, ax = plt.subplots(figsize = (12, 8))
    ax.bar(govt_grouped.index.values, govt_grouped['pt_attempt_percent'], color = 'blue')
    ax.bar(govt_grouped.index.values, govt_grouped['pt_suc_percent'], color = 'red', width = .5)
    # N = len(attempted_coups_govtype.index)
    plt.xticks(rotation=90, fontsize = 14)
    plt.yticks(rotation=0, fontsize = 14)
    plt.tight_layout(pad=3, h_pad=None, w_pad=None, rect=None)
    # ticklocations = np.arange(0,N)
    # ax.set_xticks(ticks = ticklocations -1)
    ax.set_title('Coups and Coup Attempts by Government Type (percent)', fontsize = 18)
    fig.savefig('../images/coupsbygovtpercent.png')



    # add a column for tenure in years instead of months, and then aggregate by tenure
    reign_df['tenure_years'] = reign_df['tenure_months']//12
    attempted_coups_tenure = reign_df.groupby('tenure_years').sum()['pt_attempt'].sort_index()
    suc_coups_tenure = reign_df.groupby('tenure_years').sum()['pt_suc'].sort_index()

    fig, ax = plt.subplots(figsize = (12, 8))
    ax.bar(attempted_coups_tenure.index, attempted_coups_tenure, color = 'blue', label = 'Coups Attempts')
    ax.bar(attempted_coups_tenure.index, suc_coups_tenure, color = 'red', width = .5, label = 'Successful Coups')
    # N = len(attempted_coups_govtype.index)
    plt.xticks(rotation=0, fontsize = 14)
    plt.yticks(rotation=0, fontsize = 14)
    # ticklocations = np.arange(0,N)
    # ax.set_xticks(ticks = ticklocations -1)
    ax.set_xlim(-1, 25)
    ax.set_title("Coup Attempts vs Leader's Tenure, Years", fontsize = 18)
    ax.legend(loc = 'best')
    ax.set_ylabel('Coups', fontsize = 14)
    ax.set_xlabel("Leader's Tenure, Years", fontsize = 14)
    fig.savefig('../images/coupsbyleadertenure.png')

    # creating pie charts for lived experiences (this uses the joined dataframe df_drop instead of just the reign dataframe)

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
    fig, ax = plt.subplots(figsize = (12, 12))
    ax.pie(experience_percentage_dict3.values(), explode = explode, labels= experience_percentage_dict3.keys(), startangle = 70, rotatelabels=True)
    ax.set_title('How People Were Ruled, 1950-2006', fontsize = 18)
    plt.tight_layout(pad=3, h_pad=None, w_pad=None, rect=None)
    fig.savefig('../images/ruledpiecomplex.png')

    #plot a correlation matrix
    plot_corr(df_drop)


