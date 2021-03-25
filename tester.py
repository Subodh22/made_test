import pandas as pd

df=pd.DataFrame(columns=["degree","video_id"])
jo={"degree":"c","video_id":"j"}
df=df.append(jo,ignore_index=True)
df.to_csv('./pending/ss.csv', mode='a', header=False,index=False)