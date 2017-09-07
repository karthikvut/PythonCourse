import pandas as pd

users = pd.read_csv("occupationdata.txt",sep='|')
# print(users.head(25))
# print(users.tail(10))
# print("Row Count:",users.shape[0])
# print("No. of Columns",users.shape[1])
# print("Columns are:",users.columns)
# print("Index:",users.index)
# print("DataType",users.dtypes)

print("Occupation:",users.occupation)
print("Count of Distinct Occupations:",len(users.occupation.unique()))
print("Frequent Occupation:",users.occupation.value_counts()[:1])
print("Summarize Data Frame:",users.describe())
print("Summarize Columns:",users.describe(include="all"))
print("Summarize Occupation:",users['occupation'].describe())
print("Mean Age of users:",users.age.mean())
print("Age with least occurence:",users.age.value_counts().tail(1))




