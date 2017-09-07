import pandas as pd

df = pd.read_csv("student-mat.csv")
print(df.head(3))

df_sliced = df.loc[:,'school':'guardian']
print(df_sliced.head(3))

def capitalize(x):
    return x.upper()

print("capitalized Mjob",df.Mjob.apply(capitalize).head(5))
print("capitalized Fjob",df.Fjob.apply(capitalize).head(5))

df_sliced['Mjob'] = df_sliced['Mjob'].apply(capitalize)
df_sliced['Fjob'] = df_sliced['Fjob'].apply(capitalize)

print(df_sliced.tail(5))

def majority(x):
    if x > 17:
        return True
    else:
        return False

df_sliced['legal_drinker']=df_sliced['age'].apply(majority)

def mul10(x):
    if type(x) is str:
        return x
    elif type(x) is int:
         return 10*x
    else:
        return

df_slice_new = df_sliced.applymap(mul10)

print("Mul10:",df_slice_new.head(5))









