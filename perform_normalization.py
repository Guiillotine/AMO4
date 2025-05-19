import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("datasets/credit2.txt", sep=',', index_col=0)

scaler = MinMaxScaler()

df_new = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

df_new.to_csv("datasets/credit2.txt")
