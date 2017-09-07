import pandas as pd


crime = pd.read_csv("crimerates.csv")
print(crime.head(2))

print("Column Types",crime.info())

crime['Year']=pd.to_datetime(crime['Year'], format='%Y')

print(crime.info())

crime = crime.set_index('Year')

print(crime.index)

del crime['Total']

print("Group by year and sum by values",crime.groupby('Year').agg('sum'))



# def caldecade(x):
#     year = x.strftime("%Y")
#     yearx = year[:3].join('0')
#     return(yearx)

print("Dangerous decade to live:",crime.idxmax(0))

#caldecade(x1)

