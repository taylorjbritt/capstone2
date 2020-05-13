import numpy as np
import pandas as pd


if __name__ == '__main__':
# read in dataframes
    reign_df = pd.read_csv('../data/REIGN_2020_5.csv')
    nmc_df = pd.read_csv('../data/NMC_5_0.csv')
    trade_df = pd.read_csv('../data/COW_trade_3.0/national_trade_3.0.csv')

# add yearcode columns to link the dataframes
    reign_df['yearcode'] = reign_df['ccode']*10000 + reign_df['year']
    nmc_df['yearcode'] = nmc_df['ccode']*10000 + nmc_df['year']
    trade_df['yearcode'] = trade_df['ccode']*10000 + trade_df['year']

# join the dataframes on 'yearcode'
    joint_df = reign_df.join(trade_df.set_index('yearcode'), on='yearcode', how = 'inner', rsuffix = '_tradedf' )
    joint_df = joint_df.join(nmc_df.set_index('yearcode'), on='yearcode', how = 'inner', rsuffix = '_nmcdf' )


    print(joint_df.columns)
