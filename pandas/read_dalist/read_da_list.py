#%%
import pandas as pd

df = pd.read_excel("DA-list Software Sirius.xlsx", sheet_name="Issues", header=9)
df.to_pickle("list.pkl")
# %%
df = pd.read_pickle("list.pkl")

#%% Or csv
df.to_csv('da-list.csv', index=False)
dfc = pd.read_csv('da-list.csv')

# %%
df.at[297,'#'] = 'B500'
df2 = pd.read_pickle("list.pkl")
df.compare(df2)

# %% Test comparing new list with two new rows to old
# Save old without last two lines
df = pd.read_pickle("list.pkl")
df.drop([296,297], axis=0, inplace=True)
df.to_pickle("old.pkl")
df_old = df
df_cur = pd.read_pickle("list.pkl")

# %%
df_all = df_cur.merge(df_old.drop_duplicates(), how='left', indicator=True)
df_new = df_all.loc[df_all['_merge'] == 'left_only']
df_new
# %%
