import pandas as pd

df1 = pd.read_csv('days.csv')
df1['combined'] = df1['days'] + df1['department']
# create a pivot table with counts
pivot_table = pd.pivot_table(df1, index=['combined'], aggfunc='size')

# print the pivot table
print(pivot_table)

import pandas as pd
import itertools

# list of days of the week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# generate all possible combinations of 3 days in alphabetical order, with no repeats
combinations = list(itertools.combinations(days, 3))

# sort each combination in alphabetical order and join them into a single string
combinations = [' '.join(sorted(c)) for c in combinations]

# create a pandas dataframe with the combinations as the only column
df2 = pd.DataFrame({'days': combinations})

# print the dataframe
print(df2)

df_pivottable = pivot_table.reset_index()

df_merged = df2.merge(df_pivottable, how='left',left_on='days',right_on='days')
df_merged.columns = ['days','counts']
df_merged['counts'] = df_merged['counts'].fillna(0)
df_merged['rarity'] = df_merged['counts']/sum(df_merged['counts'])
print(df_merged)




#melted_df = df1.melt(id_vars=['days'], var_name='department',)
#
#print(melted_df)