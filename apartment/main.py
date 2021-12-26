# 데이터 분석
import pandas as pd

## 1. 데이터 읽어오기
apt = pd.read_csv('주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv')

## 2. 데이터 확인하기
print(apt.info())
# print(apt.isnull().sum())

## 3. 데이터 정리하기
apt['분양가격'] = pd.to_numeric(apt['분양가격(㎡)'], errors='coerce')
apt['평당분양가격'] = apt['분양가격'] * 3.3
apt['전용면적'] = apt['규모구분'].str.replace('전용면적', '')
apt['전용면적'] = apt['전용면적'].str.replace('초과', '~')
apt['전용면적'] = apt['전용면적'].str.replace('이하', '')
apt['전용면적'] = apt['전용면적'].str.replace(' ', '').str.strip()
print(apt.groupby(['지역명', '전용면적'])['평당분양가격'].mean().unstack())
print(apt.groupby(['연도', '지역명'])['평당분양가격'].mean().unstack())
### DataFrame에서 제공하는 함수를 사용해서 열이나 행을 변환
## 4. 데이터 확인하기
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
data = apt.groupby(['연도'])['평당분양가격'].mean()
print(data)

plt.title('연도별 평당분양가격')
plt.xlabel('연도')
plt.ylabel('평당분양가격')
plt.plot(data)
plt.show()