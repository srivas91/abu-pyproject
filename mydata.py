import pandas as pd
df = pd.read_csv('C:\\users.\\niit\\student1.csv')
s = df['stuname'] == 'abu siddick'
print(df[s]['email id'])
m=df[s]['email id'].to_string()
print(m)
print(type(m))