import pandas as pd

chipo = pd.read_csv("chipotledata.txt",sep='\t')

print("Name and Price of Items:", chipo[['item_name','item_price']])

print("Sort by Item Name:", chipo['item_name'].sort_values())

#print(chipo.item_price.head(5).map(lambda x:x.strip('$')))
print("Quantity of Most expensive Item:",chipo.item_price.map(lambda x:x.strip('$')).astype(float).sort_values(ascending=False).head(1))

print("Number of times Veggie bowl ordered",len(chipo[chipo.item_name=='Veggie Salad Bowl']))

print("More than one can soda orders:",len(chipo[ (chipo.item_name=="Canned Soda") & (chipo.quantity > 1) ]))






