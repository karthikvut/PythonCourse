import pandas as pd


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
            'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

regiment = pd.DataFrame(raw_data,columns=['regiment','company','name','preTestScore','postTestScore'])

print(regiment.head(1))

#

regiment_nh = regiment[regiment['regiment'] == 'Nighthawks']

print(regiment_nh)

print("Mean PreTestScore for Nighthawks\n", regiment_nh.groupby('regiment').preTestScore.agg('mean'))

print("General Statistics by company\n", regiment.groupby('company').describe())

print("Mean PreTestScores by regiment and company\n",regiment.groupby(['regiment','company']).preTestScore.agg('mean'))

print("Mean PreTestScores by regiment and company without indexing\n",regiment.groupby(['regiment','company']).preTestScore.agg('mean').unstack())

regiment_rc = regiment.groupby(['regiment','company'])

print("No. of Observations:",regiment_rc.size())

for name, group in regiment.groupby('regiment'):
    print(name)
    print(group)




