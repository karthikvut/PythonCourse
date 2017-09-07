import pandas as pd

users = pd.read_csv("occupationdata.txt",sep='|')
print("Mean Age per occupation\n",users.groupby('occupation').age.mean())

def gender_to_num(x):
    if x == 'M':
        return 1
    else:
        return 0

users['gender_n'] = users['gender'].apply(gender_to_num)

print("Male Mean per occupation\n",(users.groupby('occupation').gender_n.sum()/users.occupation.value_counts()*100).sort_values(ascending=False))


print("Min and Max ages per occupation\n",users.groupby('occupation').age.agg(['min','max']))

print("Min and Max ages per Gender and Occupation\n", users.groupby(['occupation','gender']).age.agg(['min','max']))

gender_ocup = users.groupby(['occupation','gender']).agg({'gender':'count'})

occup_count=users.groupby(['occupation']).agg(['count'])

print(gender_ocup.columns)

print(occup_count.columns)

occup_gender = gender_ocup.div(occup_count,level=0) * 100
#
print(occup_gender.loc[:,'gender'])






