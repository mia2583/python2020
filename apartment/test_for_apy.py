import pandas as pd

apt = pd.read_csv("주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv")

#print(apt.head())
#print(apt.info())

apt["분양가격"] = pd.to_numeric(apt["분양가격(㎡)"], errors="coerce")
apt["평당분양가격"] = apt["분양가격"]*3.3

apt['전용면적'] = apt['규모구분'].str.replace('전용면적', '')
apt['전용면적'] = apt['전용면적'].str.replace('초과', '~')
apt['전용면적'] = apt['전용면적'].str.replace('이하', '')
apt['전용면적'] = apt['전용면적'].str.replace(' ', '').str.strip()
y=apt.groupby(['지역명', '전용면적'])['평당분양가격'].mean().unstack()


import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')


plt.title("연도별 평당분양가격")
plt.ylabel("평당분양가격")
plt.xlabel("연도")
plt.plot(y)
plt.show()


















''''import pandas as pd


apt = pd.read_csv("주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20200430.csv")

#print(apt.head())
#print(apt.info())

#x =apt["연도"]

#apt["분양가격(㎡)"]

apt["분양가격"] = pd.to_numeric(apt["분양가격(㎡)"], errors="coerce")
apt["평당분양가격"] = apt["분양가격"]*3.3

#apt.groupby(['지역명', '전용면적'])    #지역명과 전용면적을 묶음(행-x, 열-y)4
apt['전용면적'] = apt['규모구분'].str.replace('전용면적', '')
apt['전용면적'] = apt['전용면적'].str.replace('초과', '~')
apt['전용면적'] = apt['전용면적'].str.replace('이하', '')
apt['전용면적'] = apt['전용면적'].str.replace(' ', '').str.strip()
y=apt.groupby(['지역명', '전용면적'])['평당분양가격'].mean().unstack()
#y = apt.groupby(['지역명', '전용면적'])['평당분양가격'].mean()

print(apt.head())

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

plt.title("연도별 평당분양가격")
plt.ylabel("평당분양가격")
plt.xlabel("연도")
plt.plot(y)
plt.show()
'''
