import pandas as pd
import matplotlib.pyplot as plt

#파일 읽어오기
titanic = pd.read_csv("titanic.csv")

#제대로 출력되었는지 확인
#print(titanic.head())
#print(titanic.tail())

#생존자 시각화
#survived 열을 추출
#print(titanic['Survived']==1)
survived = len(titanic[titanic['Survived']==1])
dead = len(titanic[titanic['Survived']==0])
#print(survived)

#시각화1
#plt.bar(0, survived)
#plt.bar(1, dead, bottom=survived)
#plt.show()

#시각화2
'''graph_data = pd.DataFrame([survived, dead])
graph_data.index = ["Survived", "Dead"]
graph_data.plot(kind="bar", stacked =True)'''
#plt.show()

#시각화3
def bar_char(feature) : #feature은 열을 의미
    survived = titanic[titanic['Survived']==1][feature].value_counts()
    dead = titanic[titanic['Survived']==0][feature].value_counts()
    graph_data = pd.DataFrame([survived, dead])
    graph_data.index = ["Survived", "Dead"]
    graph_data.plot(kind="bar", stacked =True)
    plt.show()

bar_char('Pclass')



import re
c = re.compile('Mr\.') #그냥 .으로 적으면 뒤에 무엇이든 와도 되는 표현식으로 해석
for i in titanic['Name']:
    i
    #print(c.findall(i))
