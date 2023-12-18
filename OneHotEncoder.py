import pandas as pd
import numpy as np

dataset={"Col1" : ['a','b','c','a','b','c'],
         "Col2" : ["DEl","Mum","Kol","Kol","Del","Mum"],
         "Num" : [1,2,3,4,5,6]
    }
df=pd.DataFrame(dataset)
print(df)
categorical_columns = ["Col1","Num"]
OH_data=pd.get_dummies(df, columns=categorical_columns)
print(OH_data)
