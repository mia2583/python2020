#윌리를 찾아라.
#0. opencv 설치
# conda install -c conda-forge opencv
# 1. 배경이미지 불러오기
import cv2
import numpy as np

img_back = cv2.imread('find_waldo.jpg')
# 2. 색 변경(칼라-> 흑백)
img_back_gray = cv2.cvtColor(img_back, cv2.COLOR_BGR2GRAY)
# 3. 윌리 이미지 불러오기
template = cv2.imread('Waldo.jpg', cv2.IMREAD_GRAYSCALE)
# 4. 템플릿 매칭을 사용해서 검색
ret = cv2.matchTemplate(img_back_gray, template, cv2.TM_CCOEFF_NORMED)
# 5. 찾았으면 사각형 표시
loc = np.where(ret >= 0.7)
#print(loc)

w, h = template.shape[::-1]
found_w , found_h = loc[::-1]

for pt in zip(found_w, found_h) :
    cv2.rectangle(img_back, pt, (pt[0]+w, pt[1]+h), (0 , 255, 0), 3)

cv2.imshow('Waldo!', img_back)
cv2.waitKey(0)

# 6. 저장
cv2.imwrite('found_waldo.png', img_back)
