# Hanterar DA-listan med Pandas

Läser in DA-listan för Sirius så här:

```python
import pandas as pd
df = pd.read_excel("DA-list Software Sirius.xlsx", sheet_name="Issues", header=9)
```

Eftersom rubrikerna börjar på rad 10 sätts header till 9.
Visa vilka kolumner som finns:

```python
df.columns
```

Visa unika värden på Units

```python
df['Unit'].unique()
```

En DataFrame består av flera Serier, för att plocka en individuell serie (kolumn):

```python
s = df['Unit']
```

För att få en boolean tabell över var alla UI rader finns.

```python
df['Unit'] == 'UI'
```

Lägg in resultatet i en [DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) för att en ny DataFrame med de aktuella raderna.

```python
df2 = df.loc[df['Unit'] == 'UI']
```

Spara och läs tillbaka listan som en pickle

```python
df.to_pickle("list.pkl")
df = pd.read_pickle("list.pkl")
```

Eller som csv, sätt `index=False` så att det inte läggs till index-rader

```python
df.to_csv('da-list.csv', index=False)
dfc = pd.read_csv('da-list.csv')
```

[Jämför dataframes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html) Testar det genom att byta ut Issue på sista raden (med at), ladda tillbaka den sparade df och jämför.

```python
df.at[297,'#'] = 'B500'
df2 = pd.read_pickle("list.pkl")
df.compare(df2)
```

> Men man kan bara använda compare om tabellerna has samma storlek vilket inte löser mitt problem, jag vill hitta nya rader.
Testar [denna lösning](https://stackoverflow.com/a/47107164)

```python
# Test comparing new list with old
# Create old without last two lines
df = pd.read_pickle("list.pkl")
df.drop([296,297], axis=0, inplace=True)
df.to_pickle("old.pkl")
df_old = df
df_cur = pd.read_pickle("list.pkl")

df_all = df_cur.merge(df_old.drop_duplicates(), how='left', indicator=True)
df_new = df_all.loc[df_all['_merge'] == 'left_only']
```




