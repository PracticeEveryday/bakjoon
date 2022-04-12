# 터렛 내 조규현과 백승환
# 상대 마린(류재명)까지의 위치를 계산해라

# 조규현 좌표(x1, y1) 백승환의 자표 (x2, y2)
# 조규현 - 류재현 r1 , 백승환 류재명 r2
# 류재명이 있을 수 있는 좌표의 수
'''

4. 중심거리와 두 원의 위치 관계 <출처: 네이버 지식백과>

반지름의 길이가 r1인 원과 r2인 원의 중심거리(두 점 사이의 거리)를 d라고 할 때,
  |r1 - r2| 또는 r1 + r2와의 크기를 비교하면, 두 원의 위치 관계를 알 수 있다.

r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
r1 + r2 = d 이면 두 원은 외접한다.
|r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
|r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
|r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.
(x-a)**2 + (y-b)**2 = r**2
'''
import math

N = int(input())

for i in range(N):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

  if distance == 0 and r1 == r2 :
    print(-1)
  elif distance == abs(r1-r2) or distance == abs(r1+r2) :
    print(1)
  elif abs(r1-r2) < distance< abs(r1+r2) :
    print(2)
  else:
    print(0)

