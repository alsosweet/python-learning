__author__ = 'lwq'
import pandas as pd
import string
df = pd.DataFrame(columns=['home_team', 'away_team'])
df = df.append(pd.Series(['a', 'b'], index=['home_team', 'away_team']), ignore_index=True)
df = df.append(pd.Series(['d', 'c'], index=['home_team', 'away_team']), ignore_index=True)
df = df.append(pd.Series(['c', 'd'], index=['home_team', 'away_team']), ignore_index=True)
df = df.append(pd.Series(['b', 'a'], index=['home_team', 'away_team']), ignore_index=True)

"""
alpha = string.ascii_lowercase

dic_alpha = {ltr: alpha.index(ltr) for ltr in alpha }

to_bin = lambda i: '{0:05b}'.format(i)
dic_alpha_bin = {key : to_bin(val) for key,val in dic_alpha.items()}

df['bit0'] = df['home_team'].apply(lambda x: dic_alpha_bin[x])
df['bit1'] = df['away_team'].apply(lambda x: dic_alpha_bin[x])
"""
alpha = string.ascii_lowercase

dic_alpha = {ltr: alpha.index(ltr) for ltr in alpha }

to_bin = lambda i: '{0:05b}'.format(i)
dic_alpha_bin = {key : list(to_bin(val)) for key,val in dic_alpha.items()}

lst_c1 = ['bit0','bit1','bit2','bit3','bit4']
lst_c2 = ['bit5','bit6','bit7','bit8','bit9']

df[lst_c1] = df['home_team'].apply(lambda x: pd.Series(dic_alpha_bin[x]))
df[lst_c2] = df['away_team'].apply(lambda x: pd.Series(dic_alpha_bin[x]))
print(df)