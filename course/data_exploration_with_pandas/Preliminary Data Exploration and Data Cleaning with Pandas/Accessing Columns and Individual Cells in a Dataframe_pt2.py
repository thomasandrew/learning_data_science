import pandas as pd 

df = pd.read_csv('salaries_by_college_major.csv')

df = df.dropna()

print(df['Mid-Career Median Salary'].max())
print(df['Mid-Career Median Salary'].idxmax())
print(df['Undergraduate Major'][8])
print(df.loc[8])

print("-------------------------------\n\nLowest Starting Salary:\n")

print(df['Starting Median Salary'].min())
print(df['Undergraduate Major'].loc[df['Starting Median Salary'].idxmin()])
