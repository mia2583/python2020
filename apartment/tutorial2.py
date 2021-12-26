# 데이터 분석
# 1. 데이터 읽어오기
# 1-1 파이썬으로 데이터를 open
# 1-2 반복문을 사용해서 필요한 데이터를 추출 
# 2. 데이터 확인하기
# 2-1 숫자나 문자인지 확인해서 반환
#   예 ) "1"과 1은 다른 것
# 2-2 누락된 데이터가 있는지 확인
# 3. 데이터 정리하기
# 3-1 데이터 변환
# 3-2 누락 데이터 정
# 4. 데이터 확인하기


# 데이터 분석
# 1. 데이터 읽어오기
#   pandas를 이용해서 dataFrame으로 변환
# 2. 데이터 확인하기
#   dataFrame에서 제공하는 함수 사용해서 확인
# 3. 데이터 정리하기
#   dataFrame에서 제공하는 함수 사용해서 행이나 열을 변환
# 4. 데이터 확인하기


# 데이터 분석
# 1. 데이터 읽어오기
import pandas as pd
apt = pd.read_csv("주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv")
# 2. 데이터 확인하기
'''print(apt.info())   #통계치가 필요하면 describe()
print(apt[:5])
print(apt.head())
print(apt[:-5])
print(apt.tail())
print(apt.isnull().sum())   #isnull()만 하면 bool index'''

# 3. 데이터 정리하기
#apt['분양가격'] = apt['분양가격(㎡)']    #그대로 복사
#apt['분양가격'] = pd.to_numeric(apt['분양가격(㎡)']) #NaN가 있을때는 에러가 남
'''apt['분양가격'] = pd.to_numeric(apt['분양가격(㎡)'], errors="coerce")
apt['평당분양가격'] = apt['분양가격'] * 3.3'''

apt['전용면적'] = apt['규모구분'].str.replace('전용면적', '')
apt['전용면적'] = apt['전용면적'].str.replace('초과', '~')
apt['전용면적'] = apt['전용면적'].str.replace('이하', '')
apt['전용면적'] = apt['전용면적'].str.replace(' ', '').str.strip()
print(apt.groupby(['지역명', '전용면적'])['평당분양가격'].mean().unstack())
print(apt.groupby(['연도', '지역명'])['평당분양가격'].mean().unstack())

# 4. 데이터 확인하기
print(apt.info())
print(apt.head())

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
data = apt.groupby(['연도'])['평당분양가격'].mean()
print(data)

plt.title('연도별 평당분양가격')
plt.xlabel('연도')
plt.ylabel('평당분양가격')
plt.plot(data)
plt.show()
