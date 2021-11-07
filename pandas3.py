import pandas as pd

df = pd.read_csv("pika.csv")
#df.info()
#print(df.head(50))
#print(df[1:11])
#print(df["Name"][1])
print(df["Name"][1:11])
