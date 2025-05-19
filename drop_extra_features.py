import pandas as pd

df = pd.read_csv("datasets/credit2.txt", sep=',', index_col=0)
df_new = df.drop(['Состоит.в.браке', 'Срок.проживания', 'Опыт.работы'], axis=1)

df_new.to_csv("datasets/credit2.txt")
