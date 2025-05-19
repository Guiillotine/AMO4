import pandas as pd

df = pd.read_csv("datasets/credit.txt", sep=";")
df_new = df[['Возраст', 'Пол', 'Состоит.в.браке', 'Доход', 'Опыт.работы', 'Срок.проживания']]


df_new.to_csv("datasets/credit2.txt")