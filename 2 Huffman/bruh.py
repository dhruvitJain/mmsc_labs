import pandas as pd

# with open ('demo.txt',mode='r') as f:
# 	str1 = f.read()
str1 = 'stallionn'
str1 = list(str1)
n = len (str1)

d = {x:str1.count(x) for x in str1}
print (d)
symbols= (list(d.keys()))
print (symbols)

frequencies = list(d.values())
print (frequencies)

d1 = {x:str1.count(x)/n for x in str1}
probabilities = list(d1.values())
print (probabilities)

final_set = list (zip(symbols,frequencies,probabilities))
print (final_set)

df = pd.DataFrame ({'Symbol':symbols, 'Frequency':frequencies, 'Probability': probabilities})
df = df.sort_values(by=['Probability'])
df.reset_index(drop=True, inplace=True)
print (df)


