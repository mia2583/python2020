#데이터 다루기
import pandas as pd

#1. 데이터 읽기
apt = pd.read_csv("주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv")    #데이터 프레임 생성

#2. 데이터 확인하기
#print(apt.describe())
#print(apt.head())   #앞의 데이터 일부 확인
print(apt.info())   #데이터 타입 확인하기

#3. 데이터 정리하기
print(apt.isnull().sum())   #비어 있는 데이터의 수 파악
#1) 분양 가격을 숫자 데이터로 변경
apt['분양가격'] = pd.to_numeric(apt['분양가격(㎡)'], errors='coerce')    #에러가 나면 무시하고 강제로 바꿔라
#print(apt['분양가격'])
#2) 평당 분양 가격 생성하기
apt['평당분양가격'] = apt['분양가격']*3.3
#print(apt['평당분양가격'])
#3) 전용면적 구하기
#4) 지역별 평당분양가격 평균을 알고 싶을때
#apt.groupby(['지역명', '전용면적'])    #지역명과 전용면적을 묶음(행-x, 열-y)
#print(apt.groupby(['지역명', '전용면적'])['평균분양가격'].mean().unstack())

#4. 데이터 시각화
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')   #폰트 변경
data = apt.groupby(['연도'])['평당분양가격'].mean()

plt.title("연도별 평당분양가격")
plt.xlabel("연도")
plt.ylabel("평당분양가격")

plt.plot(data)
plt.show()
