# Load the Pandas libraries with alias 'pd'
import pandas as pd
import numpy as np
# Read data from file 'filename.csv'
df = pd.read_csv("/Users/annawang/icloud/Documents/Twitter copy/covid5_state.csv",lineterminator='\n')

df['user_location'].replace('Null', np.nan, inplace=True)
df.dropna(subset=['user_location'], inplace=True)
is_na= df['user_location'].isnull().sum()
print(is_na)

state_Abbrev_list =['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',
                    'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM',
                    'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
                    'WV', 'WI', 'WY']



for state in state_Abbrev_list:
    # df['state_abbrev'][df['user_location'].str.contains(state, na=False)] = state
    df.loc[df['user_location'].str.contains(state, na=False), 'state_abbrev'] = state
    # df.loc[:,('new_address','user_location')].str.contains(state,na=False)] = state
print(df.head())
print(df.shape)
print(df.dtypes)
print(df[['user_location', 'state_abbrev']])


df.to_csv('covid_5_out.csv', encoding='utf-8', na_rep='Null', errors='ignore', mode='a', index=False)

df.to_csv('/Users/annawang/icloud/Documents/Twitter copy/covid_5_out1.csv', encoding='utf-8', na_rep='Null', errors='ignore', mode='a', index=False)