import pandas as pd

data = {'Num': [1,2,3,4,5,6],
        'Cat': ['Neither prime nor composite','Prime', 'Prime','Div by 2', 'Prime', 'Div by 2&3']}
df = pd.DataFrame(data)

df['Cat'] = df['Cat'].astype('category').cat.set_categories(['Neither prime nor composite', 'Prime' , 'Div by 2', 'Div by 2&3'], ordered=True).cat.codes

print(df)
