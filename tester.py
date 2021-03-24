import pandas as pd

df=pd.DataFrame(columns=["age","sex"])

df=df.append({"age":23,"sex":33},ignore_index=True)
df=df.append({"age":3,"sex":33},ignore_index=True)
print(df)