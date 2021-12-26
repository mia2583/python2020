#데이터 다루기
import pandas as pd

#1. 데이터 읽어오기
titanic = pd.read_csv("titanic.csv")    #데이터 프레임 생성

#2. 데이터 확인하기
print(titanic.describe())
print(titanic.head())   #앞의 데이터 일부 확인

#3. 데이터 정리하기

#4. 데이터 시각화
#print(titanic["Survived"])  #column의 정보를 얻기 위해서 딕셔너리
#print(titanic["Survived"]==1)   #생존한 사람인지 true, false로 출력
#print(titanic[titanic["Survived"]==1])  #titinic에서 생존자만 출력
#print(titanic[titanic["Survived"]==1]["Pclass"])  #생존한 사람들의 pclass를 알고 싶을 때
#print(titanic[titanic["Survived"]==1]["Pclass"].value_counts())    #전체 값을 알고 싶을때(표)

import matplotlib.pyplot as plt
x = titanic[titanic["Survived"]==1]["Pclass"].value_counts()
y = titanic[titanic["Survived"]==0]["Pclass"].value_counts()
print(x,y)

plt.title("Titanic Survived of Pclass")
plt.xlabel("X")
plt.xlabel("Y")
#plt.bar(x)  #height가 없어서 오류가 남

graph_data = pd.DataFrame([x,y])    #x와 y를 합침
graph_data.plot(kind = "bar", stacked=True)
plt.show()
