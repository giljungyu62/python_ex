# 회전하는 각도와 전진하는 길이를 입력 받아 정오각형을 그려 봅시다.
# 정오각형의 내각은 72도입니다.

import turtle

t = turtle.Turtle() # 그림 그리기 준비 완료!
t.shape('turtle') # 아이콘 설정

angle = 45
length = 100
t.speed(1)

t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기

t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기
t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기
t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기
t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기
t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기
t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기
t.left(angle) # 왼쪽으로 angle(72)도 회전
t. forward(length) # 100픽셀 실선 그리기

