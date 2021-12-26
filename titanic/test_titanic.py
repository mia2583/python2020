import pandas as pd

df = pd.read_csv("titanic.csv")

#print(df.head())
#print(df.info())
#파일 읽기

x = df[df["Survived"]==0]["Pclass"].value_counts()
y = df[df["Survived"]==1]["Pclass"].value_counts()

import matplotlib.pyplot as plt
#plt.title("Titanic Survived of Pclass")
#plt.xlabel("x")
#plt.ylabel("y")

graph = pd.DataFrame([x, y])
graph.index=["Sur", "dead"]
graph.plot(kind="bar", stacked=True)
plt.show()

#pclass 별 살아남은 사람
